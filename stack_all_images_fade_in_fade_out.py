import numpy as np
from tqdm import tqdm

from utils import convert_image_to_array, get_all_input_images, save_array_as_image

image_directory = "./images/stacking_input"
image_files = get_all_input_images(image_directory)
print(f"Found {len(image_files)} image files.")

if not image_files:
    raise ValueError("No image files found!")

first_image_array = convert_image_to_array(image_files[0])
stacked_array = np.zeros(first_image_array.shape, dtype=np.float32)

stacked_array = None
number_of_images = len(image_files)
mid_point = (number_of_images - 1) / 2.0

for i, image_file in tqdm(
    iterable=enumerate(image_files),
    total=number_of_images,
    desc="Stacking images (fade in/out)",
):
    if mid_point > 0:
        brightness = 1.0 - abs(i - mid_point) / mid_point
    else:
        brightness = 1.0
    current_array = convert_image_to_array(image_file).astype(np.float32)
    modified_array = current_array * brightness
    if stacked_array is None:
        stacked_array = modified_array
    else:
        stacked_array = np.maximum(stacked_array, modified_array)

output_path = "./output/stacked/stacked_star_trails_fade_in_out.jpg"
save_array_as_image(image_array=stacked_array, output_path=output_path)  # type: ignore
print(f"The stacked image has been saved to {output_path}")
