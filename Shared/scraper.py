import requests
import re
from lxml import html, etree

#https://prehrajto.cz/joker-2019-cz-dabing-uhd/5e3a7f877b7ab

base = "https://prehrajto.cz/"
finder = base + "/hledej/"


def findUrls(name):
    movies = requests.get(finder + name)

    tree = html.fromstring(movies.content)
    links = tree.xpath('.//a[contains(@class, "video-item-link")]')
    return [link.get("href") for link in links]


def getMovie(url):
    r = requests.get(base + url)
    res = re.search('(?P<url>https:.{0,6}?storage.+?)\"', r.content.decode("utf-8"))
    return res.groups()

if __name__ == "__main__":
    searched = input("Input movie name: ")
    links = findUrls(searched)

    with open("urls.txt", "a") as f:
        for link in links:
            urls = getMovie(link)
            for url in urls:
                print(url)
                f.write(url + "\n")