import requests
import logging
from bs4 import BeautifulSoup

def request_soup(url):
	try:
		req = requests.get(url)
		html = req.content
		soup = BeautifulSoup(html, "lxml")
	except requests.exceptions.ConnectionError:
		logging.error("Connection with {} refused. Try again in a few minutes".format(url))
		raise ConnectionError()
	return soup

class Crawler:
	def __init__(self):
		self.title = "ImpAwards"
		self.site = "http://www.impawards.com/"
	
	def crawl(self, search_year, search_terms, possible_links=[]):
		url_base=self.site+"{}/".format(search_year)
		soup = request_soup(url_base+"std.html")
		for movie in soup.findAll('tr'):
			if movie.td.string and all(word in movie.td.string.lower() for word in search_terms):
				title = movie.td.string
				for link in movie.findAll('a',href=True):
					possible_links.append((title, link.get('href')))
					logging.debug("Added {}".format(link.get('href')))
					break
		return possible_links
		
	def get_images(self, search_year, movie_link):
		url_base=self.site+"{}/".format(search_year)
		images = [movie_link]
		soup = request_soup(url_base+movie_link)
		if not soup: return False
		if not soup.find('div',{'id':'altdesigns'}): return images
		for link in soup.find('div',{'id':'altdesigns'}):
			if link.get('href'):
				images.append(link.get('href'))
				logging.debug("Added {}".format(link.get('href')))
		return images

	def get_highest_resolution(self, search_year, img_link, all):
		url_base=self.site+"{}/".format(search_year)
		soup = request_soup(url_base+img_link)
		if not soup: return False
		hq_links = [img_link]
		print(img_link,hq_links)
		if not soup.findAll('a',href=True): return hq_links
		for link in soup.findAll('a',href=True):
			if "xlg" in link.get('href').lower() and link.get('href') not in hq_links:
				hq_links.append(link.get('href'))
		if all:
			logging.debug("Total images: {}".format(hq_links))
			return hq_links
		else:
			logging.debug("Changed from {} to {}".format(img_link, hq_links[-1]))
			return [hq_links[-1]]

	def download_img(self, search_year, img_link, dry_run):
		url_base=self.site+"{}/posters/".format(search_year)
		filename = img_link[:-4]+"jpg"
		print(img_link, filename)
		r = requests.get(url_base+filename)
		if r.status_code == 404:
			logging.error("Error 404 at {}".format(url_base+filename))
			return False
		if not dry_run:
			with open(filename, "wb") as f:
				logging.warning("Downloaded: {}".format(filename))
				f.write(r.content)
		else:
			logging.warning("DRY RUN: Should download {}".format(filename))
		return filename
