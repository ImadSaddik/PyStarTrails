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

stacked_array = convert_image_to_array(image_files[0]).astype(np.float32)
decay_factor = 0.99

for image_file in tqdm(
    iterable=image_files[1:],
    total=len(image_files) - 1,
    desc="Stacking images to form comet trails",
):
    stacked_array *= decay_factor
    current_array = convert_image_to_array(image_file)
    stacked_array = np.maximum(stacked_array, current_array)

final_image = Image.fromarray(stacked_array.astype(np.uint8))

output_directory = "./output/stacked/"
os.makedirs(output_directory, exist_ok=True)
output_path = os.path.join(output_directory, "stacked_star_trails_comet_style.jpg")
final_image.save(output_path)
print(f"Stacked image saved to {output_path}")
