from src.text.text_loader import load_text_data
from src.text.augmentation import BackTranslationAugmenter, BertAugmenter


def main():
    # Load text data
    text_data = load_text_data()

    # Initialize augmenters
    back_translation_augmenter = BackTranslationAugmenter()
    bert_augmenter = BertAugmenter()

    # Example usage
    sample_text = text_data[0]
    augmented_text_back_translation = back_translation_augmenter.augment_text(sample_text)
    augmented_text_bert = bert_augmenter.augment_text(sample_text)

    print(f"Original text: {sample_text}")
    print(f"Augmented text (Back Translation): {augmented_text_back_translation}")
    print(f"Augmented text (BERT): {augmented_text_bert}")


if __name__ == "__main__":
    main()