from datetime import datetime
import asyncio
from html import escape
import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler

from modules.nate_news_exporter import collect_news_dataframe, resolve_category


load_dotenv()
TOKEN = os.getenv("TG_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def _parse_newslist_args(args):
    category_key = "rec"
    pages = 1
    include_body = False

    normalized_args = [arg.strip().lower() for arg in (args or []) if arg.strip()]

    if normalized_args:
        category_key = normalized_args[0]

    if len(normalized_args) >= 2:
        try:
            pages = int(normalized_args[1])
            if pages < 1:
                pages = 1
        except ValueError:
            pages = 1

    if len(normalized_args) >= 3:
        include_body = normalized_args[2] in {"full", "body", "text", "1", "true", "y", "yes"}

    return category_key, pages, include_body


def _build_category_url(category, date):
    cat0, cat1, cat2 = category
    return (
        f"https://news.nate.com/{cat0}"
        f"?cate={cat1}&mid=n{cat2}&type=c&date={date}&page=1"
    )


async def newslist_command(update: Update, context):
    category_key, pages, include_body = _parse_newslist_args(context.args)
    category = resolve_category(category_key)
    target_date = datetime.now().strftime("%Y%m%d")

    try:
        df = await asyncio.to_thread(
            collect_news_dataframe,
            category,
            target_date,
            pages,
            include_body,
        )
    except Exception as exc:
        logger.exception("뉴스 수집 실패: %s", exc)
        await update.message.reply_text("뉴스 수집 중 오류가 발생했습니다.")
        return

    preview_count = min(3, len(df))
    category_name = df["category"].iloc[0] if len(df) else "카테고리"
    category_url = _build_category_url(category, target_date)

    if preview_count:
        preview_lines = []
        for _, row in df[["title", "url"]].head(preview_count).iterrows():
            title = escape(str(row["title"]))
            url = escape(str(row["url"]))
            preview_lines.append(f"- <a href=\"{url}\">{title}</a>")
        preview_titles = "\n".join(preview_lines)
    else:
        preview_titles = "없음"

    await update.message.reply_text(
        f"<a href=\"{escape(category_url)}\">[{escape(category_name)}]</a> {target_date} / {pages}page\n"
        f"수집 모드: {'본문 포함' if include_body else '제목/링크만'}\n"
        f"총 {len(df)}건\n"
        f"제목 미리보기({preview_count}건):\n{preview_titles}"
        ,
        parse_mode="HTML",
    )


application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("news", newslist_command))
application.run_polling(allowed_updates=Update.ALL_TYPES)


