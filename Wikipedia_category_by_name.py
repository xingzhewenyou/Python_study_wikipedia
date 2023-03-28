import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Category:Mathematics'
url = 'https://en.wikipedia.org/wiki/Category:Mathematics_education_by_country'
url = 'https://en.wikipedia.org/wiki/Category:Mathematics_education_in_the_United_States'
url = 'https://en.wikipedia.org/wiki/Category:Mathematics_education_in_the_United_Kingdom'
response = requests.get(url)
# print(response.content)

soup = BeautifulSoup(response.content, 'html.parser')
# print(soup)

links = []
sum = 0
for link in soup.find_all('a'):
    href = link.get('href')
    # print(href)
    # if href is not None and '/wiki/' in href and 'https://en.wikipedia.org' in href:
    if href is not None and '/wiki/' in href and '%' not in href and 'Category' in href\
            and 'commons.' not in href and 'Special:' not in href and 'https' not in href\
            and 'Category_' not in href and 'Help' not in href:
        if 'https://en.wikipedia.org' + href not in links:
            links.append('https://en.wikipedia.org' + href)
            print('https://en.wikipedia.org' + href)
            sum += 1

# print(links)
print(sum)

# for link in links:
#     response = requests.get(link)
#     print(response)
#     soup = BeautifulSoup(response.content, 'html.parser')
    # Perform further parsing or data extraction here
