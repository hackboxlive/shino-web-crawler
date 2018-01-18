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

def create_crawlers():
	for _ in range(NUMBER_OF_THREADS):
		t = threading.Thread(target=work)
		t.daemon = True
		t.start()

def work():
	while True:
		url = thread_queue.get()
		crawler.crawl_page(threading.current_thread().name, url)
		thread_queue.task_done()

def do_work(links):
	for link in links:
		thread_queue.put(link)
	thread_queue.join()
	start_crawl()

def start_crawl():
	links = file_to_set(UNCRAWLED_FILE)
	if len(links) > 0:
		print(str(len(links)) + ' links still to crawl')
		do_work(links)


create_crawlers()
start_crawl()