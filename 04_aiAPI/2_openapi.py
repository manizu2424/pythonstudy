import os
import json
import ast
from dotenv import load_dotenv
import openai
import pandas as pd

# .env 파일에서 환경 변수 로드
load_dotenv()

# OpenAI API 키 설정
api_key = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=api_key)


def parse_ai_result(text):
  cleaned = text.strip()
  if cleaned.startswith("```"):
    cleaned = cleaned.replace("```json", "").replace("```python", "").replace("```", "").strip()

  data = None
  try:
    data = json.loads(cleaned)
  except Exception:
    try:
      data = ast.literal_eval(cleaned)
    except Exception:
      return cleaned, ""

  if isinstance(data, dict):
    error_details = str(data.get("error_details", "")).strip()
    corrective_actions = str(data.get("corrective_actions", "")).strip()
    return error_details, corrective_actions

  return cleaned, ""

def get_error_and_action(user_prompt):
  system_prompt = '''1. 제품의 오류 내용 및 조치 사항이 주어질 것입니다.
  2. 제품의 오류 내용과 조치 사항을 적절히 분리하여 작성하세요.
  3. 답변은 반드시 파이썬의 딕셔너리 형태의 문자열로 작성하세요. 그 외에는 어떤 형태로도 작성하지 마세요. 매우 중요합니다.
  4. {"error_details": 제품의 오류 내용, "corrective_actions": 제품의 조치 사항} 형태로 작성하세요. 예시: {"error_details": 제품이 켜지지 않음, "corrective_actions": 전원 케이블 연결 확인}'''

  response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": user_prompt}
    ]
  )

  return response.choices[0].message.content

df = pd.read_excel("04_aiAPI\\CAD_CAM_errors.xlsx")
# print("데이터 개수 : ", len(df))
# print(df.head())

input_list = df["오류 내용 및 조치 사항"].tolist()
# for i in input_list[:5]:
#     print(i)

result_list = []
for input_text in input_list[:5]:
  result = get_error_and_action(input_text)
  result_list.append(result)

# print("5번 데이터 입력 : ", input_list[5])
# print("5번 데이터 처리 결과 : ", result_list[5])

if result_list:
  print("처리 건수 : ", len(result_list))
  print("마지막 데이터 타입 : ", type(result_list[-1]))

  test_df = df.head(5).copy()
  test_df["AI_분석결과"] = result_list
  parsed_result = [parse_ai_result(item) for item in result_list]
  test_df["error_details"] = [item[0] for item in parsed_result]
  test_df["corrective_actions"] = [item[1] for item in parsed_result]

  csv_path = "04_aiAPI\\CAD_CAM_errors_top5_result.csv"
  excel_path = "04_aiAPI\\CAD_CAM_errors_top5_result.xlsx"

  test_df.to_csv(csv_path, index=False, encoding="utf-8-sig")
  test_df.to_excel(excel_path, index=False)

  print("저장 완료:", csv_path)
  print("저장 완료:", excel_path)