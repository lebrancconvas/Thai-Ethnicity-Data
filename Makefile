venv:
	source .venv/bin/activate

scrape:
	python3 ./utils/web_scrape.py 

extract:
	python3 ./utils/pdf_extract.py  

clean:  
	rm **/*.Identifier 

list:
	ls -l  