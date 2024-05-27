from transformers import pipeline


def bert_augment(text: str, num_augs: int = 1, mask_token: str = "[MASK]")->list[str]:
    fill_mask = pipeline('fill-mask', model='bert-base-uncased')

    augmented_texts = []
    for _ in range(num_augs):
        res = fill_mask(text.replace("a", mask_token, 1))
        augmented_texts.append( res[0]['sequence'])

    return augmented_texts
