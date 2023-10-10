import glob
import cv2


def get_video_info(video_path):
    try:
        cap = cv2.VideoCapture(video_path)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
        frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        video_duration = frame_count / frame_rate  # Total video duration (seconds)
        cap.release()
        return frame_width, frame_height, frame_rate, video_duration
    except Exception:
        return None, None, None, None


data_dir = 'your_relative_path_here'  # Replace with your data directory's relative path
mp4_files = glob.glob(data_dir + "/*.mp4")

total_duration = 0
total_width = 0
total_height = 0
total_frame_rate = 0

print(f"Found {len(mp4_files)} .mp4 files:")
for idx, mp4_file in enumerate(mp4_files, start=1):
    print(f"{idx}. {mp4_file}")

    width, height, frame_rate, duration = get_video_info(mp4_file)
    if width is not None and height is not None and frame_rate is not None and duration is not None:
        total_duration += duration
        total_width += width
        total_height += height
        total_frame_rate += frame_rate

        minutes, seconds = divmod(int(duration), 60)
        hours, minutes = divmod(minutes, 60)
        print(f"Video Duration: {hours} hours {minutes} minutes {seconds} seconds")
        print(f"Resolution: {width} x {height}")
        print(f"Frame Rate: {frame_rate} frames/second")
    else:
        print(f"Failed to retrieve video information for {mp4_file}.")

average_width = total_width / len(mp4_files)
average_height = total_height / len(mp4_files)
average_frame_rate = total_frame_rate / len(mp4_files)

print("\nTotal Duration of All Videos: {:.2f} seconds".format(total_duration))
print(f"Number of Videos: {len(mp4_files)}")
print(f"Average Resolution: {int(average_width)} x {int(average_height)}")
print(f"Average Frame Rate: {average_frame_rate:.2f} frames/second")
