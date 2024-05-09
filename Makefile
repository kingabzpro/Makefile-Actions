RAW_DATA_PATH = raw_data/WHR2023.csv
PROCESSED_DATA = processed_data/WHR2023_cleaned.csv

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
		black *.py --line-length 88

process: $(RAW_DATA_PATH)
		python data_processing.py $(RAW_DATA_PATH)

analyze: $(PROCESSED_DATA)
		python data_analysis.py $(PROCESSED_DATA)

summary: ./processed_data/summary.txt
	echo "# Data Summary" > report.md
	cat ./processed_data/summary.txt >> report.md
	
	echo '\n# Data Analysis' >> report.md
	echo '\n## Correlation Heatmap' >> report.md
	echo '![Correlation Heatmap](./figures/correlation_heatmap.png)' >> report.md

	echo '\n## Happiness Score Distribution' >> report.md
	echo '![Happiness Score Distribution](./figures/happiness_score_distribution.png)' >> report.md

	echo '\n## Happiness Score vs GDP per Capita' >> report.md
	echo '![Happiness Score vs GDP per Capita](./figures/happiness_score_vs_gdp_per_capita.png)' >> report.md
	
	echo '\n## Social Support vs Happiness Relationship' >> report.md
	echo '![Social Support Happiness Relationship](./figures/social_support_happiness_relationship.png)' >> report.md
	
	echo '\n## Top 20 Countries by Happiness Score' >> report.md
	echo '![Top 20 Countries by Happiness Score](./figures/top_20_countries_by_happiness_score.png)' >> report.md
	
	cml comment create report.md

clean:
		rm -f processed_data/* **/*.png

all: install format process analyze