import threading
from queue import Queue
from crawler import crawler
from domain import *
from gen import *

DIR_NAME = 'hackboxlive'
HOME_URL = 'https://www.youtube.com'
DOMAIN_NAME = get_domain(HOME_URL)
UNCRAWLED_FILE = DIR_NAME + '/uncrawled.txt'
CRAWLED_FILE = DIR_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 4

thread_queue = Queue()
crawler(DIR_NAME, HOME_URL, DOMAIN_NAME)
