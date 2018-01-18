from html.parser import HTMLParser
from urllib import parse

class scraper(HTMLParser):

	def __init__(self, home_url, page_url):
		super().__init__()
		self.home_url = home_url
		self.page_url = page_url
		self.links = set()

	def handle_starttag(self, tag, attr):
		if tag == 'a':
			for key,val in attr:
				if key == 'href':
					url = parse.urlljoin(self.base_url, val)
					self.links.add(url)

	def page_links(self):
		return self.links

	def error(self, message):
		pass

#f = scraper()
#f.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>')