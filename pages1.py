import time

import requests
import json

# Set the API endpoint URL
url = "https://en.wikipedia.org/w/api.php"

# Set the initial parameters for the API call
params = {
    "action": "query",
    "format": "json",
    "list": "allpages",
    "aplimit": "100",  # Set the maximum number of results per API call
}

# Initialize the list of article titles
titles = []

# Loop through all the pages of results
while True:
    # Make an API call to retrieve a page of results
    response = requests.get(url, params=params)

    # Parse the JSON response to extract the article titles
    data = json.loads(response.content)
    pages = data["query"]["allpages"]
    for page in pages:
        title = page["title"]
        titles.append(title)
        if len(titles) % 400 == 0:
            print('title===========', title)
            print("目前的总数========", len(titles))
            time.sleep(40)

    # Check if there are more pages of results
    if "continue" in data:
        params["apcontinue"] = data["continue"]["apcontinue"]
    else:
        break

# Save the titles to a file
with open("article_titles.txt", "w") as file:
    for title in titles:
        file.write(title + "\n")
