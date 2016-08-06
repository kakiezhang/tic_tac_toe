default: web

install: pip

pip:
	./ve pip install -r requirements.txt

web:
	./ve python runserver.py
