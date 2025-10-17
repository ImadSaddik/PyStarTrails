import glob
import os

import numpy as np
from PIL import Image


def convert_image_to_array(image_path: str) -> np.ndarray:
    image = Image.open(image_path)
    return np.array(image)


def get_all_input_images(image_directory: str) -> list[str]:
    jpg_files = glob.glob(os.path.join(image_directory, "*.jpg"))
    png_files = glob.glob(os.path.join(image_directory, "*.png"))
    image_files = sorted(jpg_files + png_files)
    return image_files


def save_array_as_image(image_array: np.ndarray, output_path: str) -> None:
    final_image = Image.fromarray(image_array.astype(np.uint8))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_image.save(output_path)
