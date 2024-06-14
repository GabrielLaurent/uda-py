import argparse
import random

from .text_loader import load_text_data
from .augmentation import back_translation

def augment_text(text, augmentation_methods):
    augmented_text = text
    for method in augmentation_methods:
        if method == 'back_translation':
            augmented_text = back_translation.back_translate(text)
    return augmented_text


def main(args):
    data = load_text_data(args.data_path)

    augmented_data = []
    for text in data:
        augmentation_methods = args.augmentation_methods.split(',')
        augmented_text = augment_text(text, augmentation_methods)
        augmented_data.append(augmented_text)

    for original, augmented in zip(data, augmented_data):
        print(f"Original: {original}\nAugmented: {augmented}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Text Data Augmentation')
    parser.add_argument('--data_path', type=str, required=True, help='Path to the text data file.')
    parser.add_argument('--augmentation_methods', type=str, default='back_translation', help='Comma-separated list of augmentation methods (e.g., back_translation).')
    args = parser.parse_args()
    main(args)