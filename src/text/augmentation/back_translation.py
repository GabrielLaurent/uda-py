import googletrans

def back_translate(text, intermediate_lang='fr'):
    '''
    Translates a text to an intermediate language and back to the original language
    to generate a slightly different, augmented version of the text.
    '''
    translator = googletrans.Translator()
    # Translate to the intermediate language
    translated = translator.translate(text, dest=intermediate_lang)
    intermediate_text = translated.text

    # Translate back to the original language
    translated_back = translator.translate(intermediate_text, dest='en') # Assuming original language is English
    augmented_text = translated_back.text

    return augmented_text


if __name__ == '__main__':
    # Example Usage:
    original_text = "This is a simple sentence to test back translation."
    augmented_text = back_translate(original_text)
    print(f"Original Text: {original_text}")
    print(f"Augmented Text: {augmented_text}")
