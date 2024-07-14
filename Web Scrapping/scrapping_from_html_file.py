import csv
import re
from bs4 import BeautifulSoup

# Function to read HTML content from file
def read_html_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        html_content = file.read()
    return html_content

# Function to extract content, ratings, names, and dates from elements with specific class names
def extract_reviews(html_content, content_class, rating_class, name_class, date_class):
    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all elements with the specified class names
    content_elements = soup.find_all(class_=content_class)
    rating_elements = soup.find_all(class_=rating_class)
    name_elements = soup.find_all(class_=name_class)
    date_elements = soup.find_all(class_=date_class)

    # Check if any class is not found and print a message
    if not content_elements:
        print(f"Class '{content_class}' not found in the document.")
    if not rating_elements:
        print(f"Class '{rating_class}' not found in the document.")
    if not name_elements:
        print(f"Class '{name_class}' not found in the document.")
    if not date_elements:
        print(f"Class '{date_class}' not found in the document.")

    # Extract content, ratings, names, and dates from each element
    review_list = []
    for content_element, rating_element, name_element, date_element in zip(content_elements, rating_elements, name_elements, date_elements):
        # Get the text content of each element
        content = content_element.text.strip()
        rating = rating_element.text.strip()
        name = name_element.text.strip()
        date = date_element.text.strip()

        # Replace newline characters with spaces and normalize whitespace
        content = re.sub(r'\s+', ' ', content.replace('\n', ' ').replace('\r', ' '))
        rating = re.sub(r'\s+', ' ', rating.replace('\n', ' ').replace('\r', ' '))
        name = re.sub(r'\s+', ' ', name.replace('\n', ' ').replace('\r', ' '))
        date = re.sub(r'\s+', ' ', date.replace('\n', ' ').replace('\r', ' '))

        # Append the cleaned data to the list
        review_list.append((content, rating, name, date))

    return review_list

# Function to write reviews to CSV file
def write_to_csv(review_list, csv_filename):
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Content', 'Rating', 'Name', 'Date'])  # Write header
        for content, rating, name, date in review_list:
            writer.writerow([content, rating, name, date])

# List of HTML files
html_files = ['Amazonaustralia.html', 'Amazonaustralia2.html', 'Amazoncanada.html', 'Amazoncom.html', 'Amazonindia.html', 'Amazonjapan.html', 'Amazonswedon.html', 'Amazontr.html', 'amazon\Amazonuk.html']  # Add your HTML file names here

# Specify the class names you want to extract data from
content_class = 'review-text-sub-contents'
rating_class = 'review-rating'
name_class = 'a-profile-name'
date_class = 'review-date'

# Initialize an empty list to hold all reviews
all_reviews = []

# Iterate over each HTML file and extract reviews
for html_file in html_files:
    # Read HTML content from file
    html_content = read_html_file(html_file)

    # Extract reviews (content, ratings, names, and dates) from all elements with the specified class names
    reviews = extract_reviews(html_content, content_class, rating_class, name_class, date_class)

    # Add the extracted reviews to the list of all reviews
    all_reviews.extend(reviews)

# Specify the CSV file name to save the extracted data
csv_filename = 'reviews_dataset.csv'

# Write the extracted reviews to CSV file
write_to_csv(all_reviews, csv_filename)

print(f"Reviews (content, ratings, names, and dates) have been written to {csv_filename}")
