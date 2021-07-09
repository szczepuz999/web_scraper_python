# import requests
# from bs4 import BeautifulSoup
# import json
#
#
# def get_ld_json(url: str) -> dict: parser = "html.parser" req =
# requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
# soup = BeautifulSoup(req.text, parser) return json.loads("".join(
# soup.find("script", {"type": "application/ld+json"}).contents))
#
# def scraper_title(url): parser = "html.parser" req =
# requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
# soup = BeautifulSoup(req.text, parser) title = soup.findAll(
# 'title') # for i in title: #     print(i.text) return title[
# 0].text def apostrophe_fix(text): if "&apos" in text: new_text =
# text.replace("&apos;", "'") else: new_text = text return new_text
#
#
# # scraper('http://api.quotable.io/quotes/asdf')
# url = input("Input the URL:\n")
# correct_url = "www.imdb.com"
# if correct_url in url:
#     a = (get_ld_json(url))
#     # print(a["@type"])
#     if a["@type"] == "Movie" or a["@type"] == "TVSeries":
#         # x = dict(title=a["name"], description=a["description"])
#         x={}
#         x["title"] = scraper_title(url)
#         x["description"] = apostrophe_fix(a["description"])
#         print("")
#         print(x)
#     else:
#         print("\nInvalid movie page!")
# else: print("\nInvalid movie page!")
#
# # scraper_title(url)
#
# # a = (get_ld_json(url)) # print(a['trailer']['description']) #
# print(apostrophe_fix("An organized crime dynasty&apos;s aging
# patriarch t"))
#
# import requests
#
#
# def scraper(url):
#     file = open('source.html', 'wb')
#
#     r = requests.get(url)
#     if r.status_code == 200:
#         page_content = requests.get(url).content
#         file.write(page_content)
#         file.close()
#         print("\nContent saved.")
#     else:
#         print("\nThe URL returned {}!".format(r.status_code))
#
# url = "https://www.nature.com/nature/articles"
# scraper(url)
import string

import requests
import os
from bs4 import BeautifulSoup


def not_enough_hits_found():
    pass
root_folder = os.getcwd()

def scraper(url, type_of_article, page_number):
    # while not_enough_hits_found():
    os.chdir(root_folder)
    folder_name = "Page_" + str(page_number)
    os.mkdir(folder_name)
    os.chdir(folder_name)
    # url = "https://www.nature.com/nature/articles?searchType" \
    #       "=journalSearch&sort=PubDate&page=1"
    r = requests.get(url)
    parser = "html.parser"
    #     req = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup = BeautifulSoup(r.text, parser)
    articles = soup.findAll('article')

    for article in articles:

        type_item = article.find('span', {'data-test': 'article.type'})
        # we search here News type of articles only
        if type_of_article in type_item.text:
            updated_article_title = ''
            # select links
            article_news = article.find('a', {"data-track-action": "view article"})
            article_title = article_news.text

            # remove all whitespace
            article_title_no_whitespace = manipulate_title(article_title)
            updated_article_title = (article_title_no_whitespace)
            trans_table = updated_article_title.maketrans(' ', '_')
            article_title = updated_article_title.translate(
                trans_table) + ".txt"  # remove whitespace

            # print(article_title)
            article_link = "https://www.nature.com" + \
                           article_news.get('href')

            # here we create file with name of the article
            file = open(article_title, 'wb')

            # reads the content and close the file
            get_content_article_news(article, article_link, file)


def get_content_article_news(article, article_link, file):
    # if r.status_code == 200:
    r_art = requests.get(article_link)
    parser = "html.parser"
    #     req = requests.get(url, headers={'Accept-Language': 'en-US,en;q=0.5'})
    soup_art = BeautifulSoup(r_art.text, parser)

    article_body = soup_art.find('div', {'class': ['article-item__body']})
    # print(article_body.text)
    if article_body is None:

        article_body = soup_art.find('div', {'class': ['c-article-body u-clearfix']})

    stripped_article_body = article_body.text.strip()
    article_body_as_bytes = bytes(stripped_article_body, 'utf-8')
    file.write(article_body_as_bytes)
    file.close()

    # else:
    #     print("\nThe URL returned {}!".format(r.status_code))


def manipulate_title(article_title):
    updated_article_title = ''
    punctuation_chars = string.punctuation
    # punctuation_chars = punctuation_chars + "’" + '‘'

    temp_string = list(
        article_title)  # because string is not mutable we need to convert it to list and later join it

    for i in range(len(temp_string)):

        # checking whether the char is punctuation.
        if temp_string[i] in punctuation_chars:
            # Printing the punctuation values
            # print("Punctuation: " + i)
            temp_string[i] = ''
            # print(updated_article_title)
        # if last char is space
        if temp_string[i] == ' ' and i == (len(temp_string) - 1):
            temp_string[i] = ''

    updated_article_title = "".join(temp_string)
    return updated_article_title

url = "https://www.nature.com/nature/articles"


number_of_pages = int(input('how may pages?: '))
type_of_article = input('type of article?? :')

# loop outside scraper function but need to provide iteration number to the function so
# file handling can store files in proper folders.

# url = "https://www.nature.com/nature/articles?searchType" \
#       "=journalSearch&sort=PubDate&page=1"
for i in range(number_of_pages):
    iterable_link = "https://www.nature.com/nature/articles?searchType" \
       "=journalSearch&sort=PubDate&page=" + str(i+1)
    scraper(iterable_link, type_of_article, page_number=i+1)

print("\nContent saved.")