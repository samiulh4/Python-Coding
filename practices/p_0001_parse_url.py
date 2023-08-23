import time
from urllib.parse import urlparse


def url_parser(url):
    parts = urlparse(url)
    directories = parts.path.strip('/').split('/')
    queries = parts.query.strip('&').split('&')
    elements = {
        'scheme': parts.scheme,
        'netloc': parts.netloc,
        'path': parts.path,
        'params': parts.params,
        'query': parts.query,
        'fragment': parts.fragment,
        'directories': directories,
        'queries': queries,
    }
    return elements


if __name__ == '__main__':
    start_time = time.time()

    #url = "http://flyandlure.org:8081/articles/fly_fishing/fly_fishing_diary_july_2020?q=word&b=something#anchor"
    urls = [
        'https://www.google.com/search?q=how+to+dispose+of+a+corpse&oq=how+to+dispose+of+a+corpse&aqs=chrome..69i57j69i64.4925j1j7&sourceid=chrome&ie=UTF-8',
        'https://tales.as/101-things-to-do-with-a-dead-body_9780997711639?utm_source=google-shopping&utm_medium=cpc&utm_campaign=',
        'https://www.worldofbooks.com/en-gb/books/hugh-whitemore/disposing-of-the-body/9781872868271#NGR9781872868271',
        'https://www.google.com/search?q=where+to+buy+hydrofluoric+acid&oq=where+to+buy+hydrofl&aqs=chrome.1.69i57j0l2j0i10j0i10i395j0i395i457j0i10i395l2.8058j1j7&sourceid=chrome&ie=UTF-8'
    ]
    for url in urls:
        print(url_parser(url))
        print('-------------------------------\n')

    end_time = time.time()
    execution_time = end_time - start_time
    print("Total execution time:", execution_time, "seconds")
