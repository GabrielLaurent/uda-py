import os
from PIL import Image


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp')):
            images.append(os.path.join(folder, filename))
    return images
