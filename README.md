# PyStarTrails

![Thumbnail](./images/thumbnail.jpg)

This repository allows you to create star trails images and timelapse videos using Python. The project uses [numpy](https://github.com/numpy/numpy) for image stacking and [imageio](https://github.com/imageio/imageio) for timelapse generation. Currently, you can run the provided Python scripts manually. In the future, I plan to add a GUI (Graphical User Interface) to make the process even easier.

## Live demo

https://github.com/user-attachments/assets/a23a6de4-e19d-4c2e-8bec-afd0c538a003

## Features

### Stack images

You can stack multiple images to create a star trails effect. You have three scripts that control the shape of the trails:

- [stack_all_images.py](./stack_all_images.py): This is the basic script that stacks all images together. It does not apply any special effects to the trails.
- [stack_all_images_comet_style.py](./stack_all_images_comet_style.py): This script creates a comet-style effect, where the trails have a fading effect, making them look like comets.
- [stack_all_images_fade_in_fade_out.py](./stack_all_images_fade_in_fade_out.py): This script creates trails that fade in and fade out.

Here are images generated using each of the three scripts:

| Basic stacking | Comet style | Fade in/out |
|:--------------:|:-----------:|:-----------:|
| ![stacked_star_trails.jpg](./images/stacked_star_trails.jpg) | ![stacked_star_trails_comet_style.jpg](./images/stacked_star_trails_comet_style.jpg) | ![stacked_star_trails_fade_in_out.jpg](./images/stacked_star_trails_fade_in_out.jpg) |

### Create timelapse videos

Before creating a timelapse video, use the [generate_timelapse_frames.py](./generate_timelapse_frames.py) script to generate frames from your images. After generating the frames, you can create a timelapse video using the [create_timelapse_video.py](./create_timelapse_video.py) script.

Here is the timelapse that I generated from my star trails images in 60 FPS:

![timelapse_60fps.gif](./images/timelapse_60fps.gif)

## Usage

First, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/ImadSaddik/PyStarTrails.git
cd PyStarTrails
```

Install the [uv](https://github.com/astral-sh/uv) package manager if you don't have it already:

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Now, update the project's environment:

```bash
uv sync
```

To stack images, run one of the stacking scripts. For example, to use the basic stacking script:

```bash
uv run python stack_all_images.py
```

To create a timelapse video, first generate the frames:

```bash
uv run python generate_timelapse_frames.py
```

Then, create the timelapse video:

```bash
uv run python create_timelapse_video.py
```
