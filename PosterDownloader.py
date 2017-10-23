#F del Mazo - initial commit July 2017
#https://github.com/FdelMazo/
#federicodelmazo@hotmail.com

from impawards import Crawler
import argparse
import logging
import shutil
import os

def poster_downloader(search_terms=None, search_year=None, flags={}):
	if not search_terms:
		search = input("\n Write a movie with the year at the end (ex: The Dark Knight 2008): ")
		search = search.lower().strip().split(' ')
		search_terms, search_year = search[:-1],search[-1]
	if not search_year.isdigit():
		print("You must specify the year at the end")
		return poster_downloader()
	logging.debug("Searching for " + ' '.join(search_terms).title() + "({})".format(search_year))
	crawler = Crawler()
	possible_links = crawler.crawl(search_year, search_terms)
	if len(possible_links) == 0:
		print("No movies found")
		return poster_downloader()
	elif len(possible_links) == 1:
		title, movie_link = possible_links[-1]
	else:
		for i, tuple in enumerate(possible_links, 1):
			print("{:<3} -  {}".format(i, tuple[0]))
		selection = input("\n Which Movie? [write number] ").lower()
		logging.debug("Press return to stop ")
		while not selection.isdigit() or not 0 < int(selection) <= len(possible_links) and selection != "":
			if selection == "": return poster_downloader()
			selection = input("Just write the number: ").lower()
		title,movie_link = possible_links[int(selection) - 1]
	logging.info("Found: {}".format(title))
	images = crawler.get_images(search_year,movie_link)
	if not images: return False, False
	best_images = []
	for img in images:
		best_images.append(crawler.get_highest_resolution(search_year,img))
	files = []
	if not best_images: return False, False
	for img in best_images:
		filename = crawler.download_img(search_year,img, flags.get('dry_run'))
		files.append(filename)
	return files, title.replace(':', ' ')

def move_files(files, movie_name, dry_run):
	dir = "Posters/" + movie_name
	if not dry_run:
		os.makedirs("Posters", exist_ok=True)
		logging.warning("Posters directory created")
		os.makedirs(dir, exist_ok=True)
		logging.warning("{} directory created".format(dir))
		for file in files:
			try:
				shutil.move(file, dir)
				logging.warning("Moved {} to {}".format(file,dir))
			except Error as e:
				logging.error(e)
				pass
	else:
		logging.warning("DRY RUN: Should create Posters directory")
		logging.warning("DRY RUN: Should create {} directory".format(dir))
		for file in files:
			logging.warning("DRY RUN: Should move {} to {}".format(file,dir))


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file',help='Bath download from a txt file')
	parser.add_argument('-y', '--no-confirm', help='No input required from you', action='append_const', const=("no_confirm",True), dest='flags')
	parser.add_argument('--dry-run', help='Only show what would be done', action='append_const', const=("dry_run",True), dest='flags')

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-v', '--verbose', help='Verbose logging', action='store_const', const=logging.DEBUG, dest='loglevel')
	group.add_argument('-q', '--quiet', help='Only log warnings', action='store_const', const=logging.WARN, dest='loglevel')

	args = parser.parse_args()
	flags = dict(args.flags) if args.flags else {}
	logging.basicConfig(level=args.loglevel or logging.INFO)

	if args.file:
		txt = open(args.file)
		for i, movie in enumerate(txt):
			if not movie: break
			search = movie.lower().strip().split(' ')
			search_terms, search_year = search[:-1], search[-1]
			try:
				poster_downloader(search_terms,search_year,flags)
			except KeyboardInterrupt as e:
				logging.error(e)
				pass
		txt.close()
	else:
		try:
			files, movie_name = poster_downloader(flags=flags)
			move_files(files, movie_name, flags.get('dry_run'))
		except KeyboardInterrupt as e:
			logging.error(e)
			pass

main()
