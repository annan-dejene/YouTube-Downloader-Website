from pytube import YouTube
from io import BytesIO


def downloader(url):
  buffer = BytesIO()
  try:
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension="mp4").first()
    if stream:
      stream.stream_to_buffer(buffer)
      buffer.seek(0)
      file_name = f'{yt.title}.mp4'
      return 'Success', buffer, file_name
    else:
      return 'Error', 'No available streams for the provided URL', None
  except Exception as e:
    return 'Error', e, None
