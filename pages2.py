import requests
import json
import re
import time

# Define the API endpoint and parameters
url = "https://en.wikipedia.org/w/api.php"
params = {
    "action": "query",
    "format": "json",
    "list": "allpages",
    "aplimit": "500",
}

# Loop through all the pages of results until we reach the desired number of titles
titles = []
max_titles = 100  # Change this to the desired number of titles
while len(titles) < max_titles:
    # Make an API call to retrieve a page of results
    response = requests.get(url, params=params)
    print('11111111')

    # Parse the JSON response to extract the article titles
    data = json.loads(response.content)
    pages = data["query"]["allpages"]
    print(pages)
    for page in pages:
        print('22222222')
        title = page["title"]
        # Use regular expressions to filter out article titles that do not start with a number or a letter
        if re.match(r"^[0-9a-zA-Z!].*", title):
            titles.append(title)
            print(title)

            # Check if we have reached the desired number of titles
            if len(titles) >= max_titles:
                break

    # Check if there are more pages of results
    if "continue" in data:
        params["apcontinue"] = data["continue"]["apcontinue"]
        # Pause for 5 seconds to avoid hitting the API rate limit
        time.sleep(5)
    else:
        break

# Save the article titles to a file
with open("article_titles.txt", "w") as f:
    for title in titles:
        f.write(title + "\n")
