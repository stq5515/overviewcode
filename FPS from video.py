import cv2
import os
video_folder = 'relative_path_to_video_folder'
output_folder = 'relative_path_to_output_folder'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(video_folder):
    if filename.endswith('.mp4'):
        video_path = os.path.join(video_folder, filename)
        cap = cv2.VideoCapture(video_path)
        frame_count = 0

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame_count += 1
            frame_filename = os.path.join(output_folder, f'{filename}_frame_{frame_count:04d}.jpg')
            cv2.imwrite(frame_filename, frame)

        cap.release()

        print(f'Successfully extracted {frame_count} frames from {filename}.')
print('All videos processed.')