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
		self.crawl_page('init', crawler.home_url)

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
			
