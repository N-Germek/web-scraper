from http.server import BaseHTTPRequestHandler
import requests
from bs4 import BeautifulSoup


def scrape(url):
    # URL = 'https://en.wikipedia.org/wiki/Peanut_butter'
    page = requests.get(url)
    # print(page.content)
    soup = BeautifulSoup(page.content, "html.parser")
    # print(soup)

    results = soup.find(title="Wikipedia:Citation needed")
    # print(results.text)

    titles = [result.find_parent("p").text for result in results]
    return titles
    print(titles)

    # paragraph = link_soup.select("paragraph")[1]
    # print(paragraph[1])
    # list_items = paragraph.select("div", "div", "div", "div", "p")
    # print(list_items)
    # for title in titles:
    #     print(title.text)

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


def get_citations_needed_count(url):
    paragraphs = scrape(url)
    return len(paragraphs)


def get_citations_needed_report(URL):
    soup_results = scrape(URL)
    return "\n".join([soup.strip() for soup in soup_results])


if __name__ == "__main__":
    URL = 'https://en.wikipedia.org/wiki/Inca_Empire'
    print(scrape(URL))
    print(get_citations_needed_count(URL))
    print(get_citations_needed_report(URL))
