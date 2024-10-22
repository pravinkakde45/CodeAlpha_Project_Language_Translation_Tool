from googletrans import Translator

def translate_text(text, src_language, dest_language):
    # Create a Translator object
    translator = Translator()
    
    # Translate the text
    translation = translator.translate(text, src=src_language, dest=dest_language)
    
    # Return the translated text
    return translation.text

if __name__ == "__main__":
    # Taking user inputs for text and languages
    text_to_translate = input("Enter the text you want to translate: ")
    source_language = input("Enter the source language code (e.g., 'en' for English): ")
    destination_language = input("Enter the destination language code (e.g., 'fr' for French): ")
    
    # Call the translation function
    translated_text = translate_text(text_to_translate, source_language, destination_language)
    
    # Display the translated text
    print(f"Translated Text: {translated_text}")
