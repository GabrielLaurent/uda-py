# uda - Unsupervised Data Augmentation

## Project Overview

The 'uda' project explores Unsupervised Data Augmentation techniques for image and text data. It leverages Python and focuses on implementing and evaluating different augmentation strategies to improve model performance without labeled data.

## Project Structure

The project is structured as follows:

- `data`: Contains datasets used for experimentation.
- `docs`: Contains project documentation.
- `models`:  (Intended for) Storing trained models.
- `notebooks`: Jupyter notebooks for experimentation and analysis.
- `src`:
    - `image`: Contains code related to image data augmentation.
        - `augmentation`: Contains different image augmentation policies (e.g., RandAugment).
    - `text`: Contains code related to text data augmentation.
        - `augmentation`: Contains different text augmentation techniques (e.g., back translation, BERT augmentation).

## Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd uda
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    # venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage Examples

### Image Data Augmentation

1.  Navigate to the image directory:
    ```bash
    cd src/image
    ```

2.  Run the `main.py` script (example):
    ```bash
    python main.py  # Or a specific command to run an experiment
    ```

    (See `src/image/main.py` and related files for details on available options.)

### Text Data Augmentation

1.  Navigate to the text directory:
    ```bash
    cd src/text
    ```

2.  Run the `main.py` script (example):
    ```bash
    python main.py  # Or a specific command to run an experiment
    ```

    (See `src/text/main.py` and related files for details on available options.)

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## License

(Insert License information here, e.g., MIT License)