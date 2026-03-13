# pytubefix: pytube의 개선 버전 라이브러리 (YouTube 다운로드 지원)
from pytubefix import YouTube
import os

def get_video_and_audio(url):
  """
  YouTube URL을 받아 오디오(mp3)와 비디오(mp4)를 각각 다운로드하는 함수.
  반환값: (오디오 파일 경로, 비디오 파일 경로)
  """
  # YouTube 객체 생성 (영상 메타데이터 및 스트림 정보 로드)
  yt = YouTube(url)

  # ── 오디오 다운로드 ──────────────────────────────────────
  # 오디오 전용 스트림 중 첫 번째 항목 선택
  audio = yt.streams.filter(only_audio=True).first()
  # 05_media 폴더에 다운로드 (기본 확장자는 webm 또는 mp4)
  audio_file = audio.download(output_path="05_media")
  # 확장자를 .mp3로 변경하기 위해 파일명과 확장자 분리
  base, ext = os.path.splitext(audio_file)
  new_audio_file = base + ".mp3"
  # 파일명 변경 (실제 인코딩 변환 없이 확장자만 교체)
  os.rename(audio_file, new_audio_file)
  print(f"오디오 다운로드 완료: {new_audio_file}")

  # ── 비디오 다운로드 ──────────────────────────────────────
  # mp4 형식 중 가장 높은 해상도의 스트림 선택
  video = yt.streams.filter(file_extension="mp4").get_highest_resolution()
  # 05_media 폴더에 다운로드
  video_file = video.download(output_path="05_media")
  print(f"비디오 다운로드 완료: {video_file}")

  return new_audio_file, video_file

# 다운로드할 YouTube 영상 URL
url = "https://youtu.be/8WYz-UEcLks?si=9li0LTNwxEt43gBD"
# 함수 호출: 오디오·비디오 파일 경로 반환
audio_file, video_file = get_video_and_audio(url)