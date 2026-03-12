from gtts import gTTS

def text_to_speech(file_path_input, lang='ko', file_path='output.mp3'):
  try:
    with open(file_path_input, 'r', encoding='utf-8') as file:
      text = file.read()
  except FileNotFoundError:
    print("파일을 찾을 수 없습니다.")
    return
  except (PermissionError, UnicodeDecodeError, OSError) as e:
    print(f"파일 읽기 오류: {e}")
    return
  
  tts = gTTS(text=text, lang=lang)
  tts.save(file_path)
  print(f"음성 파일이 '{file_path}'로 저장되었습니다.")

input_text = "05_media\\tts_example_text.txt"
lang = 'ko'
output_file_path = "05_media\\output_gtts.mp3"
text_to_speech(file_path_input=input_text, lang=lang, file_path=output_file_path)