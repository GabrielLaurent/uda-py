import argparse

from src.text.data import load_data
from src.text.augmentation.back_translation import back_translate
from src.text.augmentation.bert_augmentation import bert_augment


def main(augmentation_type: str, text: str):

    if augmentation_type == "back_translation":
        augmented_text = back_translate(text)
    elif augmentation_type == "bert_augmentation":
        augmented_text = bert_augment(text)
    else:
        raise ValueError("Invalid augmentation type")

    print(f"Original text: {text}")
    print(f"Augmented text: {augmented_text}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Text augmentation script')
    parser.add_argument('--augmentation_type', type=str, required=True, help='Type of augmentation (back_translation, bert_augmentation)')
    parser.add_argument('--text', type=str, required=True, help='Text to augment')
    args = parser.parse_args()

    main(args.augmentation_type, args.text)
