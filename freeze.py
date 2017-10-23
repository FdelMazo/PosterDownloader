#F del Mazo - initial commit July 2017
#https://github.com/FdelMazo/
#federicodelmazo@hotmail.com

from cx_Freeze import setup, Executable

build_exe_options = {
	"packages": ["bs4", "shutil", "lxml", "os", "requests", "queue", "idna"],
	"includes": ["impawards"]
	}

setup(  name = "Poster Downloader",
        version = "1.0",
        description = "Webscraper for downloading movie posters in the highest resolution available",
        author = 'F del Mazo',
		author_email = 'federicodelmazo@hotmail.com',
		url = 'https://github.com/FdelMazo/PosterDownloader/releases',
		options = {"build_exe": build_exe_options},
        executables = [Executable("PosterDownloader.py")]
)