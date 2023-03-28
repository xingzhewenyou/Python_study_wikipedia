# 完美，GPT的意义堪比仓颉造字，天雨粟，鬼夜哭
import time

import requests, re
from bs4 import BeautifulSoup


# Define the function to extract links to pages up to a certain depth
def extract_links_to_depth(url, max_depth):
    visited_pages = set()
    all_links = set()
    pages_to_visit = [(url, 0)]

    # Loop until there are no more pages to visit or max depth is reached
    while pages_to_visit:
        # Get the next page to visit and mark it as visited
        page_url, depth = pages_to_visit.pop(0)
        visited_pages.add(page_url)
        # print('page_url====', page_url)

        # Stop visiting pages beyond max depth
        if depth > max_depth:
            continue

        # Find all links on the current page and add them to the set of links
        soup = BeautifulSoup(requests.get(page_url).text, 'html.parser')
        # print('soup=======', soup)
        links = []
        links_finally = []
        pattern1 = r'href="(.*?)"'
        pattern2 = r'title=(.*?)&'
        try:
            # for link in soup.find('div', class_='hlist'):
            for link in soup.find_all('a', href=True):
                # print('进入for循环============================')
                link = str(link)
                link_list = re.findall(pattern1, link)
                # print('正则匹配============')
                # print('link_list=========', link_list)
                # link_list = re.findall(pattern2, link)
                # print('link_list================', link_list)
                if link_list and 'Category:' in link_list[0]:
                    links.append(link_list)
                    # print('进入if循环================')
                    # print('links===============', links)
                    # print(type(links))
                    # print(len(links))
                    for items in links:
                        # print('进入items循环================')
                        # print('items列表===============', items)
                        items = str(items[0])
                        # print('items字符串===============', items)
                        if 'Category:' in items and 'AllPages' not in items and 'Special:' not in items\
                                and 'index' not in items and '%' not in items and 'http' not in items:
                            items = items.replace(' ', '_')
                            # print('进入category循环================')
                            # print('items===============', items)
                            if ('https://en.wikipedia.org' + items) not in all_links:
                                # links_finally.append('https://en.wikipedia.org/wiki/' + items)
                                sub_url = 'https://en.wikipedia.org' + items
                                # global_url.append('https://en.wikipedia.org/wiki/' + items)
                                pages_to_visit.append((sub_url, depth + 1))
                                all_links.add(sub_url)
                                # print('sub_url============', sub_url)
                                if len(all_links) % 500 == 0:
                                    print('目前的总链接数量：====', len(all_links))
                                    time.sleep(65)
        except:
            pass

    return all_links


# Example usage: extract links to pages up to a certain depth
url = 'https://en.wikipedia.org/wiki/Wikipedia:Contents/Categories'
max_depth = 2
# 人类维基百科，英文分类，Categories目录，13大分类，0级701个，1级14879，2级129054
all_links = extract_links_to_depth(url, max_depth)
print(all_links)
print(len(all_links))
