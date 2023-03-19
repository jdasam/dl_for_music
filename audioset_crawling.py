

if __name__ == "__main__":
  import pandas as pd
  import os
  from yt_dlp import YoutubeDL
  from tqdm import tqdm
  df = pd.read_csv("eval_segments.csv", delimiter=', ', header=2)

  DEFAULT_FS=16000
  dst_dir = 'AudioSetEval/'
  ydl_opts = {'format': 'worstaudio', 'paths': {'home': 'AudioSetEval/'}, 'external_downloader':'ffmpeg'}
  items = df['# YTID']
  items = ['https://youtu.be/'+x for x in items]
  with YoutubeDL(ydl_opts) as ydl:
    for i, url in tqdm(enumerate(items)):
      start_time = float(df['start_seconds'][i])
      output_name = f"{dst_dir}{url.split('/')[-1]}_{start_time}.wav"
      if os.path.isfile(output_name):
        continue
      os.system(f"ffmpeg -hide_banner -loglevel error -ss {str(start_time)} -t 10 -i $(yt-dlp -f 'bestaudio' -g {url}) -ar {str(DEFAULT_FS)} -- '{output_name}'")

  
