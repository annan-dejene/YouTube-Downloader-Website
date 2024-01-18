from pytube import YouTube


def downloader(url, save_path):
  try:
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True, file_extension="mp4")
    highest_res = streams.get_highest_resolution()
    highest_res.download(output_path=save_path)
    return True
  except Exception as e:
    return e, None

