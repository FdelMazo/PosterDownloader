Forma de generar ejecutable (cambiar numero de version, y depende del os la extension):
`pyinstaller posterdownloader.py -F -n PosterDownloader1.1.exe --specpath Build --distpath Releases --workpath Build`

- [ ] Install as python module

- [X] Dev Branch
- [ ] Buen project tagline
- [X] Gitignore
- [X] Carpeta Releases
- [ ] Releases Windows Linux Mac
- [X] Makefile/setup.py de build y de use. 
- [X] Modos de uso e instalacion: 
	1. Un binario doble click linux y windows (carpeta releases/binaries) 
	1. Setup.py que instala el modulo. Solo hay que hacer import videomanager y se usa. 
	1. Terminal: python3 moviemanager.... etc
- [X] Documentacion: Readme.md
	## Installation
	### Executable (Windows / Linux / Mac) 
	### Python user
	## Quick Usage
	## Complete Features
	## Developing
- [X] Arg Parser: Correr sin nada tira todas las _funciones_ y avisa que con -h se saben todas las _opciones_
- [X] Arg Parser: directory, file, input - output, quiet - verbose - debugging, dry run, no keyboard input  no confirm mode
- [X] logging en todo
- [X] Diccionario de flags y que todo reciba eso y diccionario de parametros
- [X] Buen manejo de requirements