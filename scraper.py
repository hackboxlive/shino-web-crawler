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
			for (attribute,val) in attr:
				if attribute == 'href':
#					print(val)
					url = parse.urljoin(self.home_url, val)
#					print(url)
					self.links.add(url)

	def page_links(self):
		return self.links

	def error(self, message):
		pass

#f = scraper('https://www.youtube.com','https://www.youtube.com')
#print(f.feed(''))