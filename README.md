# PosterDownloader
Py3 Webscraper for downloading official movie posters in the highest resolution available, using impawards.com as database

## Installation & Quick Usage

### Executable:
    * Download the latest executable from ['releases'](https://github.com/FdelMazo/PosterDownloader/releases)
    * After that, just start the PosterDownloader.exe (Windows) or write `./PosterDownloader` in the terminal (Linux)
	
		* Executables are generated with [PyInstaller](http://www.pyinstaller.org/) by just writing `pyinstaller posterdownloader.py`
	
### Python script:
	* Clone repo
	* `python setup.py install`
	* `python PosterDownloader.py`
	
### Python module:
	[setup.py sdist -> import Posterdownloader -> download("Dark Knight 2008")]
	
## Complete options (Only when run on terminal):
	`python PosterDownloader.py -flags` with the -flags being:
	
	* -h, --help            show this help message and exit
	* -f FILE, --file FILE  Bath download from a txt file
	* -y, --no-confirm      No confirmation required from you
	* --dry-run             Only show what would be done, without modifying files
	* -v, --verbose         Verbose/Debug logging
	* -q, --quiet           Only log file modifications