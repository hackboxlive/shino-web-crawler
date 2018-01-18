from html.parser import HTMLParser
from urllib import parse

class crawler(HTMLParser):

	def __init__(self):
		super().__init__()

	def handle_starttag(self, tag, attr):
		print(tag)

	def error(self, message):
		pass

f = crawler()
f.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1></body></html>')