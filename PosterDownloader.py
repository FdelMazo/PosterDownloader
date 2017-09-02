#F del Mazo - initial commit July 2017
#https://github.com/FdelMazo/
#federicodelmazo@hotmail.com

from impawards import Crawler
import shutil
import os
import sys

def poster_downloader(search_terms=None, search_year=None):
	if not search_terms:
		search = input("\n Write a movie with the YEAR at the end (ex: The Dark Knight 2008): ")
		search = search.lower().strip().split(' ')
		search_terms, search_year = search[:-1],search[-1]
	if not search_year.isdigit():
		print("You MUST specify the year at the end")
		return
	print(' '.join(search_terms).title(), search_year)
	crawler = Crawler()
	possible_links = crawler.crawl(search_year, search_terms)
	if len(possible_links) == 0:
		print("No movies found")
		return
	title,movie_link = possible_links[-1]
	images = crawler.get_images(search_year,movie_link)
	if not images: return
	images_xlg = []
	for img in images:
		images_xlg.append(crawler.get_xxlg(search_year,img))
	if not images_xlg: return
	os.makedirs(title.replace(':',' '),exist_ok=True)
	for img_xlg in images_xlg:
		filename = crawler.download_img(search_year,img_xlg)
		if filename: 
			try: shutil.move(filename, title)
			except: pass
	
def main():
	flag = "run"
	while flag == "run":	
		if len(sys.argv) > 1:
			archivo = open(sys.argv[1])
			for i,pelicula in enumerate(archivo):
				if not pelicula: break
				search = pelicula.lower().strip().split(' ')
				search_terms, search_year = search[:-1],search[-1]
				try: poster_downloader(search_terms, search_year)
				except KeyboardInterrupt: pass
			archivo.close()
		else:
			try: poster_downloader()
			except KeyboardInterrupt: pass
		flag = input("\nPress any key to exit or 'run' to run again: ").lower()	

main()