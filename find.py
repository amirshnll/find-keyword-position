import urllib.parse
import requests
from bs4 import BeautifulSoup
from read import read_json


def find_keyword_position(domain, keyword):
    domain = domain.lower().strip("/")
    keyword = keyword.lower()

    # request header
    headers = read_json("header.json")
    
    # construct search URL with encoded parameters
    search_url = f"https://www.google.com/search?q={urllib.parse.quote(keyword)}&num=200ie=UTF-8&hl=fa"

    # send HTTP request and parse HTML response
    try:
        response = requests.get(search_url, headers=headers)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching search results: {e}")
        return None

    # find all search result links that match the domain
    links = soup.find_all("a")
    positions = []
    counter = 0
    for i, link in enumerate(links):
        url = link.get("href")
        if url is not None:
            url = urllib.parse.unquote(url[7:])
            if "google.com" not in url.lower():
                counter += 1
                if domain in url.lower():
                    positions.append((counter, url))

    return positions
