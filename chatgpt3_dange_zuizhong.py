# 完美，GPT的意义堪比仓颉造字，天雨粟，鬼夜哭


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

        # Stop visiting pages beyond max depth
        if depth > max_depth:
            continue

        # Find all links on the current page and add them to the set of links
        soup = BeautifulSoup(requests.get(page_url).text, 'html.parser')
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
                        if 'Category:' in items:
                            items = items.replace(' ', '_')
                            if ('https://en.wikipedia.org/wiki/' + items) not in all_links:
                                # links_finally.append('https://en.wikipedia.org/wiki/' + items)
                                sub_url = 'https://en.wikipedia.org/wiki/' + items
                                # global_url.append('https://en.wikipedia.org/wiki/' + items)
                                pages_to_visit.append((sub_url, depth + 1))
                                all_links.add(sub_url)
                                print(sub_url)
        except:
            pass

        # for link in soup.find_all('a'):
        #     sub_url = link.get('href')
        #     if sub_url and not sub_url.startswith('#'):
        #         if sub_url.startswith('/') or sub_url.startswith(url):
        #             # Convert relative URLs to absolute URLs
        #             if sub_url.startswith('/'):
        #                 sub_url = url + sub_url
        #             if sub_url not in visited_pages:
        #                 pages_to_visit.append((sub_url, depth + 1))
        #                 all_links.add(sub_url)
        #                 print(sub_url)

    return all_links


# Example usage: extract links to pages up to a certain depth
url = 'https://en.wikipedia.org/wiki/Category:Mathematics'
# url = 'https://en.wikipedia.org/wiki/Category:Mathematics_education_by_country'
url = 'https://en.wikipedia.org/wiki/Category:Fields_of_mathematics'
url = 'https://en.wikipedia.org/wiki/Category:Number_theory'
url = 'https://en.wikipedia.org/wiki/Category:Prime_numbers'
url = 'https://en.wikipedia.org/wiki/Category:Mathematical_theorems'
url = 'https://en.wikipedia.org/wiki/Category:Fields_of_abstract_algebra'
max_depth = 4
# 数学0级24，,1级206，2级1107，,3级2972（40分钟）
# Fields_of_mathematics 0级23，1级347，,2级1257，看来这是数学大分类中主要的部分，就应该这样
# Number theory 0级27，,1级80, 2级163，,3级397，,4级889
# Prime numbers 0级12，1级65，,2级248，,3级585，,4级1434
# Mathematical_theorems,0级18，,1级65，,2级80，3级85，,4级86
# Fields_of_abstract_algebra ,0级18，,1级123，,2级236，,3级428，,4级855
all_links = extract_links_to_depth(url, max_depth)
print(all_links)
print(len(all_links))
