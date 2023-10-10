import os
import youtube_dl

class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

def my_hook(d):
    if d['status'] == 'finished':
        print('Done Downloading')

def download_video(youtube_id):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join('absolute_path_to_downloads_folder', '%(id)s.%(ext)s'),
        'logger': MyLogger(),
        'progress_hooks': [my_hook],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://www.youtube.com/watch?v=' + youtube_id])

def main():
    masm_file_path = r'absolute_path_to_masm_file'

    with open(masm_file_path, 'r') as masm_file:
        youtube_ids = masm_file.read().splitlines()

    for youtube_id in youtube_ids:
        download_video(youtube_id)

if __name__ == "__main__":
    main()