import os

import numpy as np
from tqdm import tqdm

from utils import convert_image_to_array, get_all_input_images, save_array_as_image

image_directory = "./images/stacking_input"
image_files = get_all_input_images(image_directory)
print(f"Found {len(image_files)} image files.")

if not image_files:
    raise ValueError("No image files found!")

stacked_array = None
output_directory = "./output/timelapse/"

for i, image_file in tqdm(
    iterable=enumerate(image_files),
    total=len(image_files),
    desc="Creating timelapse frames",
):
    current_array = convert_image_to_array(image_file)
    if stacked_array is None:
        stacked_array = current_array
    else:
        stacked_array = np.maximum(stacked_array, current_array)
    output_path = os.path.join(output_directory, f"{i:06d}.jpg")
    save_array_as_image(stacked_array, output_path)

print("Created all timelapse frames.")
