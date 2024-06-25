# src/text/text_loader.py
# Provides utility functions for loading and preprocessing text data


def load_text_data(file_path):
    # TODO: Implement text data loading and preprocessing logic here
    try:
        with open(file_path, 'r') as f:
            text = f.read()
        return text
    except FileNotFoundError:
        print(f"Error: Text file not found at {file_path}")
        return None
