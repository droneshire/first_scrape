#!/usr/bin/python
"""
Tool that scrapes data from a web page
"""
from __future__ import print_function
import argparse
import os
import sys

from scraper import Scraper

class SpxInxScraper(Scraper):
	URL = 'http://www.bloomberg.com/quote/SPX:IND'

	def __init__(self):
		super(SpxInxScraper, self).__init__(SpxInxScraper.URL)

	def parse(self):
		name_box = self.html.find('h1', attrs={'class': 'name'})
		price_box = self.html.find('div', attrs={'class':'price'})
		price = price_box.text.strip()
		name = name_box.text.strip()
		print(name)
		print(price)


def main(argv=None):
	SpxInxScraper().parse()

if __name__ == '__main__':
  sys.exit(main(sys.argv[1:]))