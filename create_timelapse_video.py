import glob
import os

import imageio.v3 as iio
from tqdm import tqdm

fps = 60
images_directory = "./output/timelapse/"
output_directory = "./output/video/"
output_filename = f"star_trails_timelapse_{fps}fps.mp4"

image_files = sorted(glob.glob(f"{images_directory}/*.jpg"))
print(f"Found {len(image_files)} frames.")

if not image_files:
    raise ValueError("No image frames found in the specified directory!")

print("Creating video from timelapse frames...")
output_path = os.path.join(output_directory, output_filename)
with iio.imopen(uri=output_path, io_mode="w", plugin="pyav") as writer:
    writer.init_video_stream(codec="libx264", fps=fps, pixel_format="yuv420p")

    for filename in tqdm(image_files, desc="Adding frames to video"):
        frame = iio.imread(filename)
        writer.write_frame(frame)

print(f"Video saved successfully to {output_path}")
