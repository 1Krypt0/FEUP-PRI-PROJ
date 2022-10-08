.PHONY: all clean

path := data

all: 
	python3 src/pipeline.py

clean:
	rm -f ./data/test.csv
	rm -f ./data/authors.csv
	rm -f ./data/spacenews_refined.csv
	rm -f ./data/spacenews_no_authors.csv
	rm -f ./data/spacenews_refined2.csv
