import os
from dotenv import load_dotenv
import openai

# .env 파일에서 환경 변수 로드
load_dotenv()

# OpenAI API 키 설정
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-5-mini",
  messages=[
    {"role": "system", "content": "당신은 친절한 조수입니다. 세줄로 요약답변해주세요."},
    {"role": "user", "content": "세종대왕이 누구인가요?"}
  ]
)

print(response.choices[0].message.content)

