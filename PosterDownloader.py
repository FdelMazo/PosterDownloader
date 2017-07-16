#F del Mazo - initial commit July 2017
#https://github.com/FdelMazo/
#federicodelmazo@hotmail.com

from impawards import Crawler
import shutil
import os

def poster_downloader():
	search = input("\n Write a movie with the YEAR at the end (ex: The Dark Knight 2008): ")
	search = search.title().strip().split(' ')
	search_terms, search_year = search[:-1],search[-1]
	if not search_year.isdigit():
		print("You MUST specify the year at the end")
		return
	crawler = Crawler()
	possible_links = crawler.crawl(search_year, search_terms)
	if len(possible_links) == 0:
		print("No movies found")
		return
	elif len(possible_links) == 1: title,movie_link = possible_links[0]
	else:
		for i,tuple in enumerate(possible_links,1):
			print("{:<3} -  {}".format(i, tuple[0]))
		selection = input("\n Which movie? (write number) ").lower()
		while not selection.isdigit() or not 0 < int(selection) <= len(possible_links) and selection != "":
			if selection == "":	return
			selection = input("Try again. Just write the number: ").lower()
		title,movie_link = possible_links[int(selection)-1]
	images = crawler.get_images(search_year,movie_link)
	images_xlg = []
	for img in images:
		images_xlg.append(crawler.get_xxlg(search_year,img))
	if not images_xlg: return
	os.makedirs(title,exist_ok=True)
	for img_xlg in images_xlg:
		filename = crawler.download_img(search_year,img_xlg)
		if filename: 
			try: shutil.move(filename, title)
			except: pass
	del possible_links[:]
	
def main():
	flag = "run"
	while flag == "run":
		try: poster_downloader()
		except KeyboardInterrupt: pass
		flag = input("\nPress any key to exit or 'run' to run again: ").lower()	
			

main()