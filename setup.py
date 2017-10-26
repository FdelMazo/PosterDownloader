#F del Mazo - initial commit July 2017
#https://github.com/FdelMazo/
#federicodelmazo@hotmail.com

from setuptools import setup
# Install with:
#	pip install setuptools
#	python setup.py install
# To generate executables (post install): 
#   pip install pyinstaller
#   Cambiar segun version y OS
#     pyinstaller posterdownloader.py -F -n PosterDownloader1.1.exe --specpath Build --distpath Releases --workpath Build


setup(  name = 'Poster Downloader',
        version = '1.0',
        description = 'Webscraper for downloading movie posters in the highest resolution available',
        author = 'F del Mazo',
		author_email = 'federicodelmazo@hotmail.com',
		url = 'https://github.com/FdelMazo/PosterDownloader/',
		install_requires = ['lxml', 'bs4', 'requests'],
)