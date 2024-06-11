import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data if not already present
try:
    stopwords.words('english')
except LookupError:
    nltk.download('stopwords')

try:
    word_tokenize('example')
except LookupError:
    nltk.download('punkt')


def load_data(data_dir):
    """Loads text data from a directory with text files.

    Args:
        data_dir (str): Path to the directory containing text files.

    Returns:
        list: A list of strings, where each string is the content of a text file.
    """
    data = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".txt"):  # Read only .txt files
            filepath = os.path.join(data_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                data.append(f.read())
    return data


def clean_text(text):
    """Cleans the text by removing HTML tags, special characters, and extra whitespace.

    Args:
        text (str): The input text.

    Returns:
        str: The cleaned text.
    """
    text = re.sub(r'<[^>]+>', '', text) # Remove HTML tags
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters and numbers
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text


def tokenize_text(text):
    """Tokenizes the text into words and removes stop words.

    Args:
        text (str): The input text.

    Returns:
        list: A list of tokens (words).
    """
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_tokens = [w for w in word_tokens if not w in stop_words]
    return filtered_tokens


if __name__ == '__main__':
    # Example Usage (assuming you have a directory named 'IMDB_raw' with text files inside)
    data_directory = 'IMDB_raw'
    if os.path.exists(data_directory):
        raw_data = load_data(data_directory)

        if raw_data:
            cleaned_example = clean_text(raw_data[0])
            tokenized_example = tokenize_text(cleaned_example)
            print("Original Text:", raw_data[0][:100], "...")
            print("Cleaned Text:", cleaned_example[:100], "...")
            print("Tokenized Text:", tokenized_example[:20], "...")
        else:
            print(f"No text files found in {data_directory}")
    else:
        print(f"{data_directory} does not exist. Please create a directory named IMDB_raw and populate it with .txt files to run the example.")
