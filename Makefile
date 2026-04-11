venv:
	source .venv/bin/activate

scrape:
	python3 ./utils/scrape.py   

clean:  
	rm **/*.Identifier 

list:
	ls -l  