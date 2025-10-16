import glob
import os

import numpy as np
from PIL import Image
from tqdm import tqdm


def convert_image_to_array(image_path: str) -> np.ndarray:
    image = Image.open(image_path)
    return np.array(image)


def save_array_as_image(array: np.ndarray, output_path: str) -> None:
    image = Image.fromarray(array.astype(np.uint8))
    image.save(output_path)


images_directory = "~/Pictures/Astronomy/Mine/Star_Trails/Oued_Amlil/JPG"
images_directory = os.path.expanduser(images_directory)
image_files = sorted(glob.glob(f"{images_directory}/*.jpg"))
print(f"Found {len(image_files)} image files.")

if not image_files:
    raise ValueError("No image files found!")

output_directory = "./output/timelapse/"
os.makedirs(output_directory, exist_ok=True)

stacked_array = convert_image_to_array(image_files[0])
output_path = os.path.join(output_directory, "000000.jpg")
save_array_as_image(stacked_array, output_path)

for i, image_file in tqdm(
    iterable=enumerate(image_files[1:]),
    total=len(image_files) - 1,
    desc="Creating timelapse frames",
):
    current_array = convert_image_to_array(image_file)
    stacked_array = np.maximum(stacked_array, current_array)
    output_path = os.path.join(output_directory, f"{i + 1:06d}.jpg")
    save_array_as_image(stacked_array, output_path)

print("Created all timelapse frames.")
