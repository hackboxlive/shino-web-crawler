from urllib.parse import urlparse

def get_domain(url):
	try:
		res = get_subdomain(url).split('.')
		#print(res)
		return res[-2] + '.' + res[-1]
	except:
		return ''


def get_subdomain(url):
	try:
		return urlparse(url).netloc
	except:
		return ''