# src/image/image_loader.py
# Provides utility functions for loading and preprocessing image data

import os
from PIL import Image


def load_image(path):
    # TODO: Implement image loading and preprocessing logic here
    try:
        img = Image.open(path)
        # Perform any necessary preprocessing steps (e.g., resizing, normalization)
        return img
    except FileNotFoundError:
        print(f"Error: Image file not found at {path}")
        return None


def load_dataset(data_dir):
  #TODO：Implement Dataset loading logic here
  pass