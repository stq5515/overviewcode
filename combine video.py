import glob
import os
import cv2
from tqdm import tqdm
import re

def sorted_alphanum(arr):
    """
    Sort strings with numbers in an alphanumeric way.
    :param arr: List of strings to be sorted
    :return: Sorted list of strings
    """
    def convert_text(text):
        """
        Extract numbers from the string and convert them; return the original string if no numbers are found.
        :param text: String to process
        :return: Tuple (a, b) where a is the string without numbers, and b is the converted result of the numeric part.
        """
        return tuple(int(s) if s.isdigit() else s for s in re.split(r'(\d+)', text))

    return sorted(arr, key=convert_text)

if __name__ == '__main__':

    fold_name = 'your_relative_path_here'
    output_name = 'output_video.mp4'
    fps = 2

    png_files = glob.glob(os.path.join(fold_name, '*'))
    # Sort the files using alphanumeric sorting
    png_files = sorted_alphanum(png_files)
    print(png_files)
    print((cv2.imread(png_files[0]).shape[1], cv2.imread(png_files[0]).shape[0]))

    writer = cv2.VideoWriter(output_name,
                             cv2.VideoWriter.fourcc(*'mp4v'),
                             fps,
                             (cv2.imread(png_files[0]).shape[1], cv2.imread(png_files[0]).shape[0]))

    for file in tqdm(png_files):
        frame = cv2.imread(file)
        writer.write(frame)

    writer.release()