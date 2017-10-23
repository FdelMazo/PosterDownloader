#F del Mazo - initial commit July 2017
#https://github.com/FdelMazo/
#federicodelmazo@hotmail.com

from setuptools import setup

setup(  name = 'Poster Downloader',
        version = '1.0',
        description = 'Webscraper for downloading movie posters in the highest resolution available',
        author = 'F del Mazo',
		author_email = 'federicodelmazo@hotmail.com',
		url = 'https://github.com/FdelMazo/PosterDownloader/',
		install_requires = ['bs4', 'lxml', 'requests'],
)