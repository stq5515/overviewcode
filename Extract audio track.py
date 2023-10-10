import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio
video_folder = 'AVFD/BoxingSpeedBag'
output_folder = 'AVFD/wav_document'
os.makedirs(output_folder, exist_ok=True)
video_folder = os.path.abspath(video_folder)

output_folder = os.path.abspath(output_folder)

for filename in os.listdir(video_folder):
    if filename.endswith(('.mp4', '.avi', '.mkv', '.mov')):
        video_path = os.path.join(video_folder, filename)
        audio_filename = os.path.splitext(filename)[0] + '.wav'
        audio_path = os.path.join(output_folder, audio_filename)
        ffmpeg_extract_audio(video_path, audio_path)
        print(f'Successfully extracted audio tracks and saved as {audio_filename}。')

print('All video audio tracks have been successfully extracted。')
