import requests
from bs4 import BeautifulSoup

# Define the URL of the homepage
homepage_url = 'https://www.example.com/'

# Send a GET request to the homepage and parse the HTML using BeautifulSoup
response = requests.get(homepage_url)
html_content = response.text
soup = BeautifulSoup(html_content, 'html.parser')

# Find all the links to the subpages on the homepage
subpage_links = soup.find_all('a', href=True)

# Loop through the subpage links and extract the text of the paragraphs
for subpage_link in subpage_links:
    # Check if the link leads to a subpage
    if 'subpage' in subpage_link['href']:
        # Generate the full URL of the subpage
        subpage_url = homepage_url + subpage_link['href']
        response = requests.get(subpage_url)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        paragraph_element = soup.find('p')
        paragraph_text = paragraph_element.text.strip()
        print(paragraph_text)
