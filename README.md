# Intel Core i7-12700K Product Sentiment Analysis <br>
This project performs sentiment analysis on customer reviews of the Intel Core i7-12700K processor, collected from Amazon and Best Buy. The analysis involves web scraping, translating, cleaning, and sentiment classification of the reviews.

## Table of Contents<br>
- Project Overview
- Workflow
> - Data Collection
> - Data Translation
> - Data Cleaning
> - Sentiment Analysis
- Results
- Requirements <br>


### Project Overview <br>
The goal of this project is to analyze customer sentiments regarding the Intel Core i7-12700K processor. We collected reviews from multiple Amazon country sites and Best Buy, processed them to ensure quality and consistency, and then applied sentiment analysis to categorize the reviews into positive, neutral, or negative sentiments.

### Workflow <br>
#### Data Collection
We started by collecting customer reviews from various Amazon country sites and Best Buy. Since accessing these reviews programmatically can be challenging due to anti-scraping measures, we downloaded the HTML pages of the reviews manually.

Methodology:

HTML Parsing: We used BeautifulSoup to parse the downloaded HTML files. Specific class names were identified within the HTML structure to extract the relevant review content, ratings, reviewer names, and dates.
Data Extraction: Extracted data was normalized to ensure consistency and saved into a CSV file named reviews_dataset.csv.
Data Translation
Since the reviews were in multiple languages, we translated the review content to English to maintain consistency for sentiment analysis.

Methodology:

Language Detection: We used the langdetect library to detect the language of each review.
Translation: Google Translate API was used to translate non-English reviews into English.
Output: The translated reviews were saved into a new CSV file named translated.csv.
Data Cleaning
To ensure the data quality, we performed several cleaning steps on the translated reviews.

Methodology:

Remove Duplicates: Duplicate reviews were removed based on the review content.
Rating Extraction: Numeric ratings were extracted and standardized.
Missing Values: Rows with missing review content or ratings were dropped.
Readability Check: An enhanced readability filter was applied to remove unreadable or gibberish reviews.
Output: The cleaned data was saved into a CSV file named cleaned_reviews.csv.
Sentiment Analysis
The core part of the project involved performing sentiment analysis on the cleaned review data.

Methodology:

Labeling: Reviews were labeled as 'Positive', 'Neutral', or 'Negative' based on their ratings.
Text Preprocessing: Reviews were tokenized, lowercased, stripped of punctuation, and stopwords were removed.
Vectorization: We used TF-IDF vectorization to convert the text data into numerical features.
Class Balancing: The Synthetic Minority Over-sampling Technique (SMOTE) was used to address class imbalance in the training data.
Model Training: A Logistic Regression model was trained using the balanced dataset. Hyperparameter tuning was performed using GridSearchCV.
Evaluation: The model was evaluated on a test set, and performance metrics such as accuracy, confusion matrix, and classification report were generated. <br>
### Results <br>
The sentiment analysis model successfully categorized customer reviews into positive, neutral, and negative sentiments. Key findings include:

- Accuracy: The model achieved a satisfactory accuracy.
- Common Themes: Visualizations like n-grams and word clouds highlighted common themes in the reviews.
- Class Distribution: SMOTE effectively balanced the class distribution, improving the model's performance on minority classes. <br>

### Requirements <br>
- Python
- BeautifulSoup
- pandas
- langdetect
- googletrans
- scikit-learn
- imbalanced-learn
- nltk
- matplotlib
- seaborn
- wordcloud
