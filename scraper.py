from http.server import BaseHTTPRequestHandler
import requests
from bs4 import BeautifulSoup


URL = 'https://en.wikipedia.org/wiki/Peanut_butter'
page = requests.get(URL)
# print(page.content)
soup = BeautifulSoup(page.content, "html.parser")
# print(soup)

results = soup.find(class_="noprint Inline-Template Template-Fact")
print(results.prettify())

titles = results.find_all("p")
# print(titles)

for title in titles:
    print(title.text)

anchors = results("a")
# print(anchors)
# print(anchors.content)

links = [anchor["href"] for anchor in anchors]
# print(links)

# python_link = links[1]
# print(python_link)

python_url = "https://en.wikipedia.org"
link_content = requests.get(python_url)
link_soup = BeautifulSoup(link_content.content, "html.parser")

# paragraph = link_soup.select("paragraph")[1]
# print(paragraph[1])
# list_items = paragraph.select("div", "div", "div", "div", "p")
# print(list_items)


def get_citations_needed_count():
    pass


def get_citations_needed_report():
    pass
