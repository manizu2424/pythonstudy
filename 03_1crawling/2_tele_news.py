import asyncio
from datetime import datetime
import logging
import os

from telegram import Update
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

from modules.nate_news_crawler import make_url_list

load_dotenv()
TOKEN = os.getenv("TG_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.DEBUG)
logger = logging.getLogger(__name__)

REC_CATEGORY = ("recent", "its", "n0601")
COM_CATEGORY = ("subsection", "its03", "n0604")


def _parse_news_args(args, raw_text=""):
    category_key = "rec"
    category = REC_CATEGORY
    pages = 1

    normalized_args = [arg.strip().lower() for arg in (args or []) if arg.strip()]

    # context.args가 비어 있는 경우를 대비해 원문 텍스트에서 보조 파싱
    if not normalized_args and raw_text:
        text_parts = raw_text.strip().split()
        if len(text_parts) >= 2:
            normalized_args = [text_parts[1].strip().lower()]
            if len(text_parts) >= 3:
                normalized_args.append(text_parts[2].strip().lower())

    if normalized_args:
        if normalized_args[0] in {"com", "computer", "internet"}:
            category_key = "com"
            category = COM_CATEGORY
        elif normalized_args[0] in {"rec", "recent"}:
            category_key = "rec"
            category = REC_CATEGORY

    if len(normalized_args) >= 2:
        try:
            pages = int(normalized_args[1])
            if pages < 1:
                pages = 1
        except ValueError:
            pages = 1

    return category_key, category, pages


async def news_command(update: Update, context):
    raw_text = update.message.text if update.message else ""
    category_key, category, pages = _parse_news_args(context.args, raw_text)
    date = datetime.now().strftime("%Y%m%d")
    logger.info("/news args=%s parsed=(%s, %s)", context.args, category_key, pages)

    try:
        url_list = await asyncio.to_thread(make_url_list, category, date, pages)
    except Exception as exc:
        logger.exception("뉴스 수집 실패: %s", exc)
        await update.message.reply_text("뉴스 수집 중 오류가 발생했습니다.")
        return

    if not url_list:
        await update.message.reply_text("수집된 뉴스가 없습니다.")
        return

    top_n = 5
    preview_links = "\n".join(url_list[:top_n])
    category_name = "컴퓨터/인터넷" if category_key == "com" else "IT 최신뉴스"

    msg = (
        f"[{category_name}] {date} / {pages}page\n"
        f"총 {len(url_list)}건\n\n"
        f"상위 {min(top_n, len(url_list))}건:\n{preview_links}"
    )
    await update.message.reply_text(msg)

application = Application.builder().token(TOKEN).build()
application.add_handler(CommandHandler("news", news_command))
application.run_polling(allowed_updates=Update.ALL_TYPES) 