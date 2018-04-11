
import urllib2
from bs4 import BeautifulSoup


class Scraper(object):

	def __init__(self, page_url):
		self.url = page_url
		page = urllib2.urlopen(self.url)
		self.html = BeautifulSoup(page, 'html.parser')

	def parse(self):
		""" Parse a specific page. Override in subclasses. """
		pass
