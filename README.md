# PosterDownloader
Py3 Webscraper for downloading official movie posters in the highest resolution available, using impawards.com as database

## Installation & Quick Usage

### Executable:
* Download the latest executable from ['releases'](https://github.com/FdelMazo/PosterDownloader/releases)
* After that, just start the PosterDownloader.exe (Windows) or write `./PosterDownloader` in the terminal (Linux)
    * Executables are generated with [PyInstaller](http://www.pyinstaller.org/) by just writing `pyinstaller posterdownloader.py`

### Python script:
* Clone repo `git clone`
* Install the dependencies `python setup.py install`
* Execute `python PosterDownloader.py`
    
### Python module:
    [setup.py sdist -> import Posterdownloader -> download("Dark Knight 2008")]
    
## Complete options (Only when run on terminal):

`python PosterDownloader.py ["The Dark Knight 2008"] -flags` with ["Movie year"] being optional and the -flags being:

* -h, --help            Show this help message and exit
* -f FILE, --file FILE  Bath download from a txt file
* -y, --no-confirm      No confirmation required from you
* --dry-run             Only show what would be done, without modifying files
* -l, --log             Log everything to PosterDownlaoder.log
* -v, --verbose         Verbose/Debug logging
* -q, --quiet           Only log file modifications

### I have a problem! How can I contact you?

The easiest would be for you to describe your problem to me in the [issues](https://github.com/FdelMazo/posterdownloader/issues) section. To make it even easier you could replicate your error (search the same movies, pass the same txt file, etc etc) but this time logging it:
`Python posterdownloader.py --log`