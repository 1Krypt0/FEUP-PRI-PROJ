.PHONY: all clean

path := data

all: run_scripts

run_scripts:
	python3 src/pipeline.py
	

clean:
	rm -f ./data/authors.csv
	rm -f ./data/spacenews_clean.csv
