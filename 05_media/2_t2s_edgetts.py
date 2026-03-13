# edge_tts: Microsoft Edge의 온라인 TTS(Text-to-Speech) 엔진을 사용하는 라이브러리
import edge_tts
# asyncio: edge_tts가 비동기 방식으로 동작하므로 async/await 실행에 필요
import asyncio

async def main():
    """텍스트 파일을 읽어 TTS로 변환한 뒤 mp3 파일로 저장하는 비동기 함수."""

    # 변환할 텍스트가 담긴 입력 파일 경로
    file_path_input = "05_media\\tts_example_text.txt"
    try:
        # UTF-8 인코딩으로 텍스트 파일 읽기
        with open(file_path_input, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return
    except (PermissionError, UnicodeDecodeError, OSError) as e:
        # 권한 오류, 인코딩 오류, 기타 OS 오류 처리
        print(f"파일 읽기 오류: {e}")
        return

    # edge_tts Communicate 객체 생성 (TTS 변환 설정)
    communicate = edge_tts.Communicate(
        text,
        voice="ko-KR-SunHiNeural",   # 한국어 여성 음성 (SunHi)
        # voice="ko-KR-InJoonNeural", # 한국어 남성 음성 (InJoon) — 필요 시 교체
        # rate="+20%",                # 말하기 속도 조절 (기본값 0%)
        # pitch="+5Hz",               # 음정(피치) 조절
        volume="+20%"                 # 볼륨을 기본값보다 20% 올림
    )

    # 변환된 음성을 mp3 파일로 저장 (비동기 처리)
    await communicate.save("05_media\\output_edge_tts.mp3")
    print(f"음성 파일이 '05_media\\output_edge_tts.mp3'로 저장되었습니다.")


# 비동기 main 함수 실행 진입점
asyncio.run(main())