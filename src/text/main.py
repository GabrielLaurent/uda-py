from src.text.augmentation import generic_augment


def main():
    text = "This is an example sentence."
    augmented_text = generic_augment(text)
    print(f"Original text: {text}")
    print(f"Augmented text: {augmented_text}")


if __name__ == "__main__":
    main()