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
- Requirements
- Conclusion <br>


### Project Overview <br>
The goal of this project is to analyze customer sentiments regarding the Intel Core i7-12700K processor. We collected reviews from multiple Amazon country sites and Best Buy, processed them to ensure quality and consistency, and then applied sentiment analysis to categorize the reviews into positive, neutral, or negative sentiments.

### Workflow <br>
#### Data Collection
We started by collecting customer reviews from various Amazon country sites and Best Buy. Since accessing these reviews programmatically can be challenging due to anti-scraping measures, we downloaded the HTML pages of the reviews manually.

**Methodology:**

*__HTML Parsing:__* We used BeautifulSoup to parse the downloaded HTML files. Specific class names were identified within the HTML structure to extract the relevant review content, ratings, reviewer names, and dates. <br>
*__Data Extraction:__* Extracted data was normalized to ensure consistency and saved into a CSV file named reviews_dataset.csv. <br>
*__Data Translation:__* Since the reviews were in multiple languages, we translated the review content to English to maintain consistency for sentiment analysis.

**Methodology:**

*__Language Detection:__* We used the langdetect library to detect the language of each review. <br>
*__Translation:__* Google Translate API was used to translate non-English reviews into English. <br>
*__Output:__* The translated reviews were saved into a new CSV file named translated.csv. <br>
*__Data Cleaning:__* To ensure the data quality, we performed several cleaning steps on the translated reviews.

**Methodology:**

*__Remove Duplicates:__* Duplicate reviews were removed based on the review content. <br>
*__Rating Extraction:__* Numeric ratings were extracted and standardized. <br>
*__Missing Values:__* Rows with missing review content or ratings were dropped. <br>
*__Readability Check:__* An enhanced readability filter was applied to remove unreadable or gibberish reviews. <br>
*__Output:__* The cleaned data was saved into a CSV file named cleaned_reviews.csv. <br>
*__Sentiment Analysis:__* The core part of the project involved performing sentiment analysis on the cleaned review data.

**Methodology:**

*__Labeling:__* Reviews were labeled as 'Positive', 'Neutral', or 'Negative' based on their ratings. <br>
*__Text Preprocessing:__* Reviews were tokenized, lowercased, stripped of punctuation, and stopwords were removed. <br>
*__Vectorization:__* We used TF-IDF vectorization to convert the text data into numerical features. <br>
*__Class Balancing:__* The Synthetic Minority Over-sampling Technique (SMOTE) was used to address class imbalance in the training data. <br>
*__Model Training:__* A Logistic Regression model was trained using the balanced dataset. Hyperparameter tuning was performed using GridSearchCV. <br>
*__Evaluation:__* The model was evaluated on a test set, and performance metrics such as accuracy, confusion matrix, and classification report were generated.


### Results <br>
The sentiment analysis model successfully categorized customer reviews into positive, neutral, and negative sentiments. Key findings include:

- **Accuracy:** The model achieved a satisfactory accuracy.
- **Common Themes:** Visualizations like n-grams and word clouds highlighted common themes in the reviews.
- **Class Distribution:** SMOTE effectively balanced the class distribution, improving the model's performance on minority classes. <br>

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

## Conclusion <br>
The sentiment analysis project for the Intel Core i7-12700K processor provides valuable insights into customer opinions and satisfaction levels across different regions. Through a comprehensive workflow involving data collection, translation, cleaning, and analysis, we were able to accurately categorize customer reviews into positive, neutral, and negative sentiments.

- **Positive Feedback:** A significant portion of reviews were positive, indicating high customer satisfaction with the Intel Core i7-12700K processor’s performance and features.
- **Common Themes:** The most frequent positive comments highlighted the processor’s speed, efficiency, and value for money. Negative comments were often related to pricing and occasional technical issues.
- **Model Performance:** The Logistic Regression model, optimized using GridSearchCV, demonstrated satisfactory accuracy in predicting review sentiments. The use of SMOTE effectively addressed class imbalance, enhancing the model's performance.
- **Insights for Improvement:** The analysis provides actionable insights for Intel to address common customer concerns and improve future product iterations.
