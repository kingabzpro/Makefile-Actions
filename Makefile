RAW_DATA_PATH = "raw_data/WHR2023.csv"
PROCESSED_DATA = "processed_data/WHR2023_cleaned.csv"

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
		black *.py --line-length 88

process: data_processing.py
		python data_processing.py $(RAW_DATA_PATH)

analyze: data_processing.py
		python data_analysis.py $(PROCESSED_DATA)

clean:
		rm -f processed_data/* **/*.png

all: install format process analyze