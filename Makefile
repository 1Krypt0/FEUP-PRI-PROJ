.PHONY: all clean

all: install_dependencies fill_missing clean_data separate_authors extract_extra

install_dependencies:
	pip install pandas	
	pip install beautifulsoup4
	pip install requests
	pip install numpy
	pip install newspaper3k

fill_missing:
	python3 src/fill_missing.py 

clean_data:
	python3 src/clean_data.py

separate_authors:
	python3 src/separate_authors.py

extract_extra:
	python3 src/extract_tags_sections.py

# Convert with pretier so that it is properly formatted
convert_formats:
	python3 src/convert_formats.py && npx prettier --write data/spacenews.json

clean:
	rm -f data/authors.csv
	rm -f data/spacenews_filled.csv
	rm -f data/spacenews_clean.csv
	rm -f data/spacenews_separated.csv
	rm -f data/spacenews.json
