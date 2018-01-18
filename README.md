# shino-web-crawler

A multi-threaded website crawler, written in Python. As of now, the crawler just gathers links from a specified base_url, and crawls through all the links having the same domain name as the base_url.

## Requirements and Usage

Python 3 or above.

1. Open the `main.py` file and change the `HOME_URL` string to the base url that you want to crawl.

2. Specify the name of the output directory that you need to get the links in.

3. Execute `main.py`.

## Future Scope

The analytics part, data storage and searching could be added as separate modules.
