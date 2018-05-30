"""Synchronously download a list of webpages and time it"""
from urllib.request import Request, urlopen
from time import time

sites = [
    "http://news.ycombinator.com/",
    "https://www.yahoo.com/",
    "https://github.com/",
    "http://deelay.me/5000/http://deelay.me/",
]


def find_size(url):
    req = Request(url)
    with urlopen(req) as response:
        page = response.read()
        return len(page)


def main():
    for site in sites:
        size = find_size(site)
        print("Read {:8d} chars from {}".format(size, site))


if __name__ == '__main__':
    start_time = time()
    main()
    print("Ran in {:6.3f} secs".format(time() - start_time))
