# PosterDownloader
Py3 Webscraper for downloading official movie posters in the highest resolution available, using impawards.com as database

<a href='https://asciinema.org/a/262714'><img src='https://i.imgur.com/E0Bpd1B.gif'></a>

## Installation & Quick Usage

### Python script:
* Clone repo `git clone https://github.com/FdelMazo/PosterDownloader.git`
* Install the dependencies `python setup.py install`
* Execute `python PosterDownloader.py`

### Executable (Windows & Linux):
* Download the latest executable from ['releases'](https://github.com/FdelMazo/PosterDownloader/releases/latest)
* After that, just start the PosterDownloader.exe (Windows) or write `./PosterDownloader` in the terminal (Linux)
    * Executables are generated with [PyInstaller](http://www.pyinstaller.org/) by just writing `pyinstaller posterdownloader.py -F`

## Usage (as Python script):

`./PosterDownloader.py ["The Dark Knight 2008"] -flags` with the movie between brackets being optional and the -flags being:

* `-h, --help`            Show this help message and exit
* `-f FILE, --file FILE`  Bath download from a txt file
* `-y, --no-confirm`      No confirmation required from you
* `-a, --all`             Download every poster, instead of only the highest resolution available
* `--dry-run`             Only show what would be done, without modifying files
* `-l, --log`             Log everything to PosterDownlaoder.log
* `-v, --verbose`         Verbose/Debug logging
* `-q, --quiet`           Only log file modifications