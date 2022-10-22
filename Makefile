.PHONY: all clean

all: run_scripts

run_scripts:
	python3 src/fill_missing.py && \
	python3 src/clean_data.py && \
	python3 src/separate_authors.py

clean:
	rm -f data/authors.csv
	rm -f data/spacenews_filled.csv
	rm -f data/spacenews_clean.csv
	rm -f data/spacenews_final.csv
