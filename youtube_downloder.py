from pytube import YouTube
from io import BytesIO


def downloader(url):
  try:
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension="mp4").first()
    if stream:
      video_data = BytesIO(stream.stream_to_buffer)
      file_name = f'{yt.title}.mp4'
      return 'Success', video_data.getValue(), file_name
    else:
      return 'Error', 'No available streams for the provided URL', None
  except Exception as e:
    return 'Error', e, None
