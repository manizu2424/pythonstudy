from pytubefix import YouTube
import os

def get_video_and_audio(url):
  yt = YouTube(url)

  audio = yt.streams.filter(only_audio=True).first()
  audio_file = audio.download(output_path="05_media")
  base, ext = os.path.splitext(audio_file)
  new_audio_file = base + ".mp3"
  os.rename(audio_file, new_audio_file)
  print(f"오디오 다운로드 완료: {new_audio_file}")

  video = yt.streams.filter(file_extension="mp4").get_highest_resolution()
  video_file = video.download(output_path="05_media")
  print(f"비디오 다운로드 완료: {video_file}")

  return new_audio_file, video_file

url = "https://youtu.be/8WYz-UEcLks?si=9li0LTNwxEt43gBD"
audio_file, video_file = get_video_and_audio(url)