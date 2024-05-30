import torch
from transformers import BertTokenizer, BertModel
import random

class BertAugmenter:
    def __init__(self, model_name='bert-base-uncased', masked_prob=0.15):
        self.tokenizer = BertTokenizer.from_pretrained(model_name)
        self.model = BertModel.from_pretrained(model_name)
        self.model.eval()
        self.masked_prob = masked_prob

    def augment_text(self, text, num_augmentations=1):
        augmented_texts = []
        for _ in range(num_augmentations):
            augmented_texts.append(self._augment_single(text))
        return augmented_texts

    def _augment_single(self, text):
        tokens = self.tokenizer.tokenize(text)
        token_ids = self.tokenizer.convert_tokens_to_ids(tokens)

        masked_token_ids = token_ids.copy()
        mask = random.sample(range(len(token_ids)), int(len(token_ids) * self.masked_prob))
        for i in mask:
            masked_token_ids[i] = self.tokenizer.mask_token_id

        input_tensor = torch.tensor([masked_token_ids])

        with torch.no_grad():
            outputs = self.model(input_tensor)
            token_embeddings = outputs.last_hidden_state

        #Simplified version: replace masked words with '[UNK]' token
        augmented_tokens = tokens.copy()
        for i in mask:
              augmented_tokens[i] = '[UNK]'

        augmented_text = self.tokenizer.convert_tokens_to_string(augmented_tokens)
        return augmented_text

if __name__ == '__main__':
    augmenter = BertAugmenter()
    text = "This is an example sentence."
    augmented_texts = augmenter.augment_text(text, num_augmentations=2)
    print(f"Original text: {text}")
    print(f"Augmented texts: {augmented_texts}")