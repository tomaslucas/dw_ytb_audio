from pytube import YouTube
import argparse
import os
from moviepy.editor import *


def download_audio_youtube(url: str, path: str, name: str):
    try:
        yt = YouTube(url)
        mp4_file = os.path.join(path, f'{name}.mp4')
        mp3_file = os.path.join(path, f'{name}.mp3')
        video = yt.streams.filter(only_audio=True).first().download(output_path=path, filename=f'{name}.mp4')
        video_clip = AudioFileClip(mp4_file)
        video_clip.write_audiofile(mp3_file)
        os.remove(mp4_file)

    except Exception as e:
        print("Error: ", e)
    return

def main():
    parser = argparse.ArgumentParser(description='Download audio from Youtube.')
    parser.add_argument('url', type=str, help='Youtube URL.')
    parser.add_argument('--path', type=str, help='Output path for audio files.', default="./audios")
    parser.add_argument('--name', type=str, help='Name for audio file.', default="temp")

    args = parser.parse_args()
    try:
        if not os.path.exists(args.path):
            os.makedirs(args.path)
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise
    
    download_audio_youtube(args.url, args.path, args.name)
    

if __name__ == "__main__":
    main()