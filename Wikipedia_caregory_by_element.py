import requests, re
from bs4 import BeautifulSoup, NavigableString, Tag

url_list = [
    'https://en.wikipedia.org/wiki/Category:Women_logicians',
    # 'https://en.wikipedia.org/wiki/Category:Mathematics',
    'https://en.wikipedia.org/wiki/Category:Mathematics_education_by_country',
    # 'https://en.wikipedia.org/wiki/Category:Mathematics_education_in_the_United_States',
]
url = 'https://en.wikipedia.org/wiki/Category:Mathematics'

# url = 'https://en.wikipedia.org/wiki/Category:Mathematics_education_by_country'
# url = 'https://en.wikipedia.org/wiki/Category:Mathematics_education_in_the_United_States'
# url = 'https://en.wikipedia.org/wiki/Category:Mathematics_education_in_the_United_Kingdom'
# url = 'https://en.wikipedia.org/wiki/Category:Mathematical_classification_systems'#没有子分类
# url = 'https://en.wikipedia.org/wiki/Category:Women_logicians'

url_globle = []


def find_all_subcategory(url_list):
    pattern = r'title="(.*?)"'
    copy_url_list = url_list
    # print('提取之前的copy_url_list', copy_url_list)
    for items1 in url_list:
        print('items1的循环', items1)
        response = requests.get(items1)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = []
        links_finally = []
        # print('提取之前的links_finally', links_finally)
        try:
            for link in soup.find('div', id='mw-subcategories'):
                link = str(link)
                link_list = re.findall(pattern, link)
                if link_list:
                    links.append(link_list)
                    for items in links[0]:
                        if 'Category:' in items:
                            items = items.replace(' ', '_')
                            links_finally.append('https://en.wikipedia.org/wiki/' + items)
                            url_globle.append('https://en.wikipedia.org/wiki/' + items)
                            # print(items)
        except:
            print('没有子分类')
        # print('删除之前的copy_url_list', copy_url_list)
        # if len(copy_url_list) > 1:
        #     del copy_url_list[0]
        #     print('删除之后的copy_url_list', copy_url_list)
        # elif len(copy_url_list) == 1:
        #     copy_url_list.clear()
        #     print('删除之后的copy_url_list', copy_url_list)
        # else:
        #     print('copy_url_list是空的')
        # print('提取之后的copy_url_list', copy_url_list)
        print('提取之后的links_finally', links_finally)
        print(len(links_finally))
        # return links_finally


# print('运行函数之前的url_list', url_list)
find_all_subcategory(url_list=url_list)
# print('运行函数之后的url_list', url_list)
# print('运行函数之后的url_globle', url_globle)
# print('url_globle的长度', len(url_globle))
# for link in links:
#     response = requests.get(link)
#     print(response)
#     soup = BeautifulSoup(response.content, 'html.parser')
# Perform further parsing or data extraction here
