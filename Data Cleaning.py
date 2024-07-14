import pandas as pd
import re

# Load the dataset
df = pd.read_csv('translated.csv')

# Display the first few rows of the dataframe
print("Initial DataFrame:")
print(df.head())

# Data Cleaning
# Remove duplicates based on 'Content'
df.drop_duplicates(subset='Content', keep='first', inplace=True)

# Extract numeric rating from the 'Rating' column
df['Rating'] = df['Rating'].apply(lambda x: float(re.findall(r'\d+\.\d+|\d+', x)[0]) if pd.notnull(x) else None)

# Drop rows with missing 'Content' or 'Rating'
df.dropna(subset=['Content', 'Rating'], inplace=True)

# Enhanced filter for unreadable reviews
def is_readable(text):
    try:
        # Check if text can be encoded and decoded without errors
        text.encode('utf-8').decode('utf-8')
        
        # Check the ratio of non-alphanumeric characters
        non_alpha_ratio = len(re.findall(r'\W', text)) / len(text)
        
        # Consider text unreadable if more than 50% of characters are non-alphanumeric
        if non_alpha_ratio > 0.5:
            return False
        
        return True
    except UnicodeDecodeError:
        return False


df = df[df['Content'].apply(is_readable)]

# Keep only 'Content' and 'Rating' columns
df = df[['Content', 'Rating']]

# Display basic statistics
print("Basic statistics:")
print(df.describe())

# Save cleaned dataset
df.to_csv('cleaned_reviews3.csv', index=False)

print("Data cleaning completed. Cleaned data saved to 'cleaned_reviews3.csv'.")
