import edge_tts
import asyncio

async def main():

    file_path_input = "05_media\\tts_example_text.txt"
    try:
        with open(file_path_input, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return
    except (PermissionError, UnicodeDecodeError, OSError) as e:
        print(f"파일 읽기 오류: {e}")
        return

    communicate = edge_tts.Communicate(
        text,
        voice="ko-KR-SunHiNeural",
        # voice="ko-KR-InJoonNeural",
        # rate="+20%",
        # pitch="+5Hz",
        volume="+20%"
    )

    await communicate.save("05_media\\output_edge_tts.mp3")
    print(f"음성 파일이 '05_media\\output_edge_tts.mp3'로 저장되었습니다.")


asyncio.run(main())