from pytube import YouTube
import argparse

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
    download_audio_youtube(args.url, args.path)
    

if __name__ == "__main__":
    main()