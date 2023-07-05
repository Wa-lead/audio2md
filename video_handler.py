import requests
from moviepy.editor import VideoFileClip
"""
downloads a video from a given url and splits the audio from the video
"""

OUTPUT_DIR = 'media'
class VideoHandler():
    
    def download_video(self, url: str, output_path: str = 'video.mp4') -> None:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(f'{OUTPUT_DIR}/video/{output_path}', 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print("Video downloaded successfully.")
        else:
            print("Failed to download video.")
            
    def split_audio(self, video_path: str, output_path: str = 'audio.mp3') -> None:
        video = VideoFileClip(video_path)
        audio = video.audio
        audio.write_audiofile(f'{OUTPUT_DIR}/audio/{output_path}')
        print("Audio extracted successfully.")