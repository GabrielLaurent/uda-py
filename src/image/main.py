import os
from src.image.image_loader import load_image


def main():
    # Example usage:
    image_path = 'data/test_image.jpg'  # Replace with your image path

    # Create a dummy image 'data/test_image.jpg' if it doesn't exist.
    # This ensures the example runs without error if the user doesn't
    # have their own image already in the data directory.
    if not os.path.exists(image_path):
        from PIL import Image
        img = Image.new('RGB', (100, 100), color='red')
        os.makedirs('data', exist_ok=True)
        img.save(image_path)

    image = load_image(image_path)

    if image:
        print(f"Image loaded successfully. Format: {image.format}, Size: {image.size}, Mode: {image.mode}")
        # You can now use the 'image' object for further processing, e.g., augmentation.
        # image.show() # uncomment if you want to display the image


if __name__ == "__main__":
    main()
