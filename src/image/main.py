import os
import sys
import argparse

from PIL import Image


# Add the project root to the python path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.append(PROJECT_ROOT)

from src.image.image_loader import load_images_from_folder
from src.image.augmentation.randaugment import RandAugment


def augment_and_save(image_dir, output_dir, num_augs=2):
    """
    Loads images from a directory, applies RandAugment, and saves the augmented images.
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    images = load_images_from_folder(image_dir)
    
    if not images:
        print(f"No images found in {image_dir}")
        return

    augmenter = RandAugment()

    for i, image in enumerate(images):
      
        img = Image.open(image)
        
        for j in range(num_augs):
          
            augmented_image = augmenter(img)
            
            # Save the augmented image
            output_path = os.path.join(output_dir, f"image_{i}_aug_{j}.png")
            augmented_image.save(output_path)
            print(f"Saved augmented image to {output_path}")



def main():
    parser = argparse.ArgumentParser(description='Apply RandAugment to images in a directory.')
    parser.add_argument('--image_dir', type=str, required=True, help='Path to the directory containing images.')
    parser.add_argument('--output_dir', type=str, required=True, help='Path to the directory to save augmented images.')
    parser.add_argument('--num_augs', type=int, default=2, help='Number of augmentations to apply to each image.')

    args = parser.parse_args()

    augment_and_save(args.image_dir, args.output_dir, args.num_augs)


if __name__ == "__main__":
    main()
