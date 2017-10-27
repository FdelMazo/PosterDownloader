#F del Mazo - initial commit July 2017
#https://github.com/FdelMazo/
#federicodelmazo@hotmail.com

from impawards import Crawler
import argparse
import logging
import shutil
import os

def poster_downloader(search=None, flags={}):
	if search:
		search = search.lower().strip().split(' ')
		search_terms, search_year = search[:-1],search[-1]
		if search_year.isdigit():    	
			logging.debug("Searching for " + ' '.join(search_terms).title() + " {}".format(search_year))
		else:
			logging.warning("You must specify the year at the end")
			return False, False
	else:
		search = input("\n Write a movie with the year at the end (ex: The Dark Knight 2008): ")
		return poster_downloader(search, flags)
	crawler = Crawler()
	possible_links = crawler.crawl(search_year, search_terms)
	if len(possible_links) == 0:
		logging.warning("No movies found")
		return False, False
	elif len(possible_links) == 1:
		title, movie_link = possible_links[-1]
	else:
		for i, tuple in enumerate(possible_links, 1):
			logging.info("\t {:<3} -  {}".format(i, tuple[0]))
		logging.debug("Press return to stop ")
		selection = input("\n Which Movie? [Number] ").lower()
		while not selection.isdigit() or not 0 < int(selection) <= len(possible_links) and selection != "":
			if not selection:
				logging.warning("User canceled action")
				del possible_links[:]
				return False, False
			selection = input("Just write the number: ").lower()
		title,movie_link = possible_links[int(selection) - 1]
	logging.info("Found {} at {}".format(title, movie_link))
	if not flags.get('no_confirm'):
		response = True if input("Do you want to download the posters for this movie? ([Y]es/[N]o): ").lower() in 'yes' else False
		if not response:
			logging.warning("User canceled action")
			del possible_links[:]
			return False, False
		else:
			logging.debug("User confirmed action")
	images = crawler.get_images(search_year,movie_link)
	if not images:
		logging.warning("No images found")
		del possible_links[:]
		return False, False
	logging.debug("Processing {} images".format(len(images)))
	best_images = []
	for img in images:
		best_images.extend(crawler.get_highest_resolution(search_year,img, flags.get('all')))
	if not best_images:
		del possible_links[:]
		return False, False
	logging.debug("Changed to a total of {} images".format(len(best_images)))
	files = []
	for img in best_images:
		filename = crawler.download_img(search_year,img, flags.get('dry_run'))
		if filename: files.append(filename)
	del possible_links[:]
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
				logging.error('Error '+e)
				pass
	else:
		logging.warning("DRY RUN: Should create Posters directory")
		logging.warning("DRY RUN: Should create {} directory".format(dir))
		for file in files:
			logging.warning("DRY RUN: Should move {} to {}".format(file,dir))


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('command_line_movie',help='Movies can be called from the CLA', nargs='?', action = 'store', default = None)
	parser.add_argument('-f', '--file',help='Bath download from a txt file')
	parser.add_argument('-y', '--no-confirm', help='No confirmation required from you', action='append_const', const=("no_confirm",True), dest='flags')
	parser.add_argument('-a', '--all', help='Download every poster, instead of only the highest resolution available', action='append_const', const=("all",True), dest='flags')
	parser.add_argument('--dry-run', help='Only show what would be done without modifying files', action='append_const', const=("dry_run",True), dest='flags')
	parser.add_argument('-l', '--log', help='Log everything to PosterDownloader.log', action='store_true')

	group = parser.add_mutually_exclusive_group()
	group.add_argument('-v', '--verbose', help='Verbose/Debug logging', action='store_const', const=logging.DEBUG, dest='loglevel')
	group.add_argument('-q', '--quiet', help='Only log file modifications', action='store_const', const=logging.WARN, dest='loglevel')
    
	args = parser.parse_args()
	flags = dict(args.flags) if args.flags else {}
	superformat = '%(levelname)s: %(message)s - %(funcName)s at %(filename)s.%(lineno)d'
	if args.log:
		console = logging.StreamHandler()
		console.setLevel(args.loglevel or logging.INFO)
		console.setFormatter(logging.Formatter(superformat))
		logging.basicConfig(level=logging.DEBUG, format=superformat, filename='PosterDownloader.log')
		logging.getLogger('').addHandler(console)
	elif args.loglevel:	logging.basicConfig(level=args.loglevel, format=superformat)
	else:  logging.basicConfig(level=logging.INFO, format='%(message)s')
	
	logging.warning("Starting...")
	
	if args.file:
		txt = open(args.file)
		for i, movie in enumerate(txt):
			if not movie: break
			try:
				files, movie_name = poster_downloader(movie,flags)
				if files and movie_name: move_files(files, movie_name, flags.get('dry_run'))
			except KeyboardInterrupt:
				logging.error('KeyboardInterrupt')
				continue
		txt.close()
	else:
		try:
			files, movie_name = poster_downloader(args.command_line_movie, flags)
			if files and movie_name: move_files(files, movie_name, flags.get('dry_run'))
		except KeyboardInterrupt:
			logging.error('KeyboardInterrupt')
			pass

main()
