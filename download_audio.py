from pytube import YouTube
import argparse
import os


def download_audio_youtube(url: str, path: str):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        video.download(output_path=path)
    except Exception as e:
        print("Error: ", e)
    return

def main():
    parser = argparse.ArgumentParser(description='Download audio from Youtube.')
    parser.add_argument('url', type=str, help='Youtube URL.')
    parser.add_argument('--path', type=str, help='Output path for audio files.', default="./audios")

    args = parser.parse_args()
    try:
        if not os.path.exists(args.path):
            os.makedirs(args.path)
    except OSError as e:
      if e.errno != errno.EEXIST:
        raise
    
    download_audio_youtube(args.url, args.path)
    

if __name__ == "__main__":
    main()