from src.text import data
import os

class TextDataLoader:
    def __init__(self, data_dir='IMDB_raw'):
        self.data_dir = data_dir

    def load_and_preprocess_data(self):
        """Loads, cleans, and tokenizes text data.

        Returns:
            list: A list of lists, where each inner list contains tokens for a text file.
        """
        if not os.path.exists(self.data_dir):
            print(f"{self.data_dir} does not exist. Please create a directory named IMDB_raw and populate it with .txt files.")
            return []

        raw_data = data.load_data(self.data_dir)
        cleaned_data = [data.clean_text(text) for text in raw_data]
        tokenized_data = [data.tokenize_text(text) for text in cleaned_data]
        return tokenized_data


if __name__ == '__main__':
    # Example Usage
    loader = TextDataLoader()
    processed_data = loader.load_and_preprocess_data()

    if processed_data:
        print("Loaded and Preprocessed Data (First 10 tokens of the first document):")
        print(processed_data[0][:10])  # Print the first 10 tokens of the first document
    else:
        print("No data loaded.")
