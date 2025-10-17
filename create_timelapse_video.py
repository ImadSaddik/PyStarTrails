import os

import imageio.v3 as iio
from tqdm import tqdm

from utils import get_all_input_images

image_directory = "./output/timelapse/"
image_files = get_all_input_images(image_directory)
print(f"Found {len(image_files)} image files.")

if not image_files:
    raise ValueError("No image frames found in the specified directory!")

print("Creating video from timelapse frames...")

fps = 60
output_directory = "./output/video/"
os.makedirs(os.path.dirname(output_directory), exist_ok=True)
output_filename = f"star_trails_timelapse_{fps}fps.mp4"
output_path = os.path.join(output_directory, output_filename)
with iio.imopen(uri=output_path, io_mode="w", plugin="pyav") as writer:
    writer.init_video_stream(codec="libx264", fps=fps, pixel_format="yuv420p")

    for filename in tqdm(image_files, desc="Adding frames to video"):
        frame = iio.imread(filename)
        writer.write_frame(frame)

print(f"Video saved successfully to {output_path}")
