import time

import requests, re
from bs4 import BeautifulSoup

# Define the base URL of the website
base_url = 'https://en.wikipedia.org/wiki/Category:Mathematics'
# base_url = 'https://en.wikipedia.org/wiki/Category:Coding_theory'
global_url = []

global depth
max_depth = 3


def crawl_page(url, max_depth):
    response = requests.get(url)
    # time.sleep(2)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    links_finally = []
    pattern = r'title="(.*?)"'
    try:
        for link in soup.find('div', id='mw-subcategories'):
            link = str(link)
            link_list = re.findall(pattern, link)
            if link_list:
                links.append(link_list)
                for items in links[0]:
                    if 'Category:' in items and 'Mathematicians' not in items and 'Mathematics by country' not in items \
                            and 'Spinors' not in items and 'Rotation in three dimensions' not in items \
                            and 'Special functions' not in items:
                        items = items.replace(' ', '_')
                        if ('https://en.wikipedia.org/wiki/' + items) not in global_url:
                            links_finally.append('https://en.wikipedia.org/wiki/' + items)
                            global_url.append('https://en.wikipedia.org/wiki/' + items)
    except:
        pass
    print('links_finally=====', links_finally)
    print('目前的深度为======', depth)
    # Recursively crawl each link that leads to a subpage
    if depth < 2:
        depth = depth + 1
        for link in links_finally:
            print(type(link), link)
            if 'Category:' in link:
                crawl_page(link,max_depth+1)


crawl_page(url=base_url, max_depth=max_depth)
print('global_url', global_url)
print('global_url的数量==============', len(global_url))

# # 第一版，遇到没有子页面的报错
# def crawl_page(url):
#     response = requests.get(url)
#     html_content = response.text
#     soup = BeautifulSoup(html_content, 'html.parser')
#     links = []
#     links_finally = []
#     pattern = r'title="(.*?)"'
#     for link in soup.find('div', id='mw-subcategories'):
#         link = str(link)
#         link_list = re.findall(pattern, link)
#         if link_list:
#             links.append(link_list)
#             for items in links[0]:
#                 if 'Category:' in items:
#                     items = items.replace(' ', '_')
#                     links_finally.append('https://en.wikipedia.org/wiki/' + items)
#     print('links_finally=====', links_finally)
#     # Recursively crawl each link that leads to a subpage
#     for link in links_finally:
#         print(type(link), link)
#         if 'Category:' in link:
#             crawl_page(link)
# crawl_page(base_url)


# 原始存档
# # Define a function to crawl a page and extract the text of the paragraphs
# def crawl_page(url):
#     response = requests.get(url)
#     html_content = response.text
#     soup = BeautifulSoup(html_content, 'html.parser')
#     paragraph_elements = soup.find_all('p')
#     for paragraph_element in paragraph_elements:
#         paragraph_text = paragraph_element.text.strip()
#         print(paragraph_text)
#
#     # Find all the links on the page
#     links = soup.find_all('a', href=True)
#
#     # Recursively crawl each link that leads to a subpage
#     for link in links:
#         if base_url in link['href']:
#             crawl_page(link['href'])
#
# # Start crawling from the homepage
# crawl_page(base_url)
