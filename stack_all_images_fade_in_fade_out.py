import glob
import os

import numpy as np
from PIL import Image
from tqdm import tqdm


def convert_image_to_array(image_path: str) -> np.ndarray:
    image = Image.open(image_path)
    return np.array(image)


images_directory = "~/Pictures/Astronomy/Mine/Star_Trails/Oued_Amlil/JPG"
images_directory = os.path.expanduser(images_directory)
image_files = sorted(glob.glob(f"{images_directory}/*.jpg"))
print(f"Found {len(image_files)} image files.")

if not image_files:
    raise ValueError("No image files found!")

first_image_array = convert_image_to_array(image_files[0])
stacked_array = np.zeros(first_image_array.shape, dtype=np.float32)

num_images = len(image_files)
mid_point = (num_images - 1) / 2.0

for i, image_file in tqdm(
    iterable=enumerate(image_files),
    total=num_images,
    desc="Stacking images (fade in/out)",
):
    if mid_point > 0:
        brightness = 1.0 - abs(i - mid_point) / mid_point
    else:
        brightness = 1.0
    current_array = convert_image_to_array(image_file).astype(np.float32)
    modified_array = current_array * brightness
    stacked_array = np.maximum(stacked_array, modified_array)

final_image = Image.fromarray(stacked_array.astype(np.uint8))

output_directory = "./output/stacked/"
os.makedirs(output_directory, exist_ok=True)
output_path = os.path.join(output_directory, "stacked_star_trails_fade_in_out.jpg")
final_image.save(output_path)
print(f"Stacked image saved to {output_path}")
