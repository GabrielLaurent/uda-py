from PIL import Image


def load_image(image_path):
    """Loads an image from the given path using PIL.

    Args:
        image_path (str): The path to the image file.

    Returns:
        PIL.Image.Image: The loaded image.
    """
    try:
        img = Image.open(image_path)
        return img
    except FileNotFoundError:
        print(f"Error: Image not found at {image_path}")
        return None
    except Exception as e:
        print(f"Error loading image: {e}")
        return None
