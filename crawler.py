from urllib.request import urlopen
from scraper import scraper
from gen import *

class crawler:

	#shared members
	dir_name = ''
	home_url = ''
	domain_name = ''
	uncrawled_file = ''
	crawled_file = ''
	queue = set()
	crawled = set()

	def __init__(self, dir_name, home_url, domain_name):
		crawler.dir_name = dir_name
		crawler.home_url = home_url
		crawler.domain_name = domain_name
		crawler.uncrawled_file = crawler.dir_name + '/uncrawled.txt'
		crawler.crawled_file = crawler.dir_name + '/crawled.txt'
		self.initialize()
		self.crawl_page('Initial crawler', crawler.home_url)

	@staticmethod
	def initialize():
		create_project(crawler.dir_name)
		create_files(crawler.dir_name, crawler.home_url)
		crawler.queue = file_to_set(crawler.uncrawled_file)
		crawler.crawled = file_to_set(crawler.crawled_file)

	@staticmethod
	def crawl_page(thread_name, page_url):
		if page_url not in crawler.crawled:
			print(thread_name + ' crawling ' + page_url)
			print('Queue ' + str(len(crawler.queue)) + ' | Crawled ' + str(len(crawler.crawled)))
			crawler.add_to_queue(crawler.get_links_from(page_url))
			crawler.queue.remove(page_url)
			crawler.crawled.add(page_url)
			crawler.update_files()

	@staticmethod
	def get_links_from(page_url):
		htm_str = ''
		try:
			ret = urlopen(page_url)
			if ret.getheader('Content-Type') == 'text/html':
				temp = ret.read()
				htm_str = temp.decode("utf-8")
			f = scraper(crawler.home_url, crawler.page_url)
			f.feed(htm_str)
		except:
			print('Error raised: could not crawl page: ' + page_url)
			return set()
		return f.page_links()
	
	@staticmethod
	def add_to_queue(links):
		for url in links:
			if url in crawler.queue:
				continue
			if url in crawler.crawled:
				continue
			if crawler.domain_name not in links:
				continue
			crawler.queue.add(url)

	@staticmethod
	def update_files():
		set_to_file(crawler.queue, crawler.uncrawled_file)
		set_to_file(crawler.crawled, crawler.crawled_file)
