#F del Mazo - initial commit July 2017
#https://github.com/FdelMazo/
#federicodelmazo@hotmail.com

from setuptools import setup
# Install with:
# 	apt-get install python3-pip
#	pip3 install setuptools
#   if required: apt-get install python3-lxml
#	python3 setup.py install
# To generate executables (post install): 
#   pip3 install pyinstaller
#   Cambiar segun version y OS
#     pyinstaller PosterDownloader.py -F -n PosterDownloader1.1.exe --specpath Build --distpath Releases --workpath Build
#	if required: /home/username/.local/bin/pyinstaller aka https://stackoverflow.com/questions/38746462/how-to-correctly-install-pyinstaller 


setup(  name = 'Poster Downloader',
        version = '1.0',
        description = 'Webscraper for downloading movie posters in the highest resolution available',
        author = 'F del Mazo',
		author_email = 'federicodelmazo@hotmail.com',
		url = 'https://github.com/FdelMazo/PosterDownloader/',
		install_requires = ['lxml', 'bs4', 'requests'],
)
