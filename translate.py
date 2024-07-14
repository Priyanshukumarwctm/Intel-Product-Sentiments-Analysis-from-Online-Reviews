import pandas as pd
from langdetect import detect
from googletrans import Translator

# Load the CSV file
file_path = 'reviews_dataset.csv'  # replace with your file path
df = pd.read_csv(file_path)

# Initialize the translator
translator = Translator()

# Function to detect language and translate to English if not already in English
def translate_to_english(text):
    try:
        lang = detect(text)
        if lang != 'en':
            translated = translator.translate(text, src=lang, dest='en')
            return translated.text
        else:
            return text
    except:
        return text

# Apply the translation function to the 'Content' column
df['Content'] = df['Content'].apply(translate_to_english)

# Save the dataframe back to a CSV file
output_file_path = 'translated.csv'  
df.to_csv(output_file_path, index=False)

print("Translation completed and saved to", output_file_path)
