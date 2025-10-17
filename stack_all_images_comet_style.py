import numpy as np
from tqdm import tqdm

from utils import convert_image_to_array, get_all_input_images, save_array_as_image

image_directory = "./images/stacking_input"
image_files = get_all_input_images(image_directory)
print(f"Found {len(image_files)} image files.")

if not image_files:
    raise ValueError("No image files found!")

stacked_array = None
decay_factor = 0.99

for i, image_file in tqdm(
    iterable=enumerate(image_files),
    total=len(image_files),
    desc="Stacking images to form comet trails",
):
    current_array = convert_image_to_array(image_file).astype(np.float32)
    if stacked_array is None:
        stacked_array = current_array
    else:
        stacked_array *= decay_factor
        stacked_array = np.maximum(stacked_array, current_array)

output_path = "./output/stacked/stacked_star_trails_comet_style.jpg"
save_array_as_image(image_array=stacked_array, output_path=output_path)  # type: ignore
print(f"The stacked image has been saved to {output_path}")
