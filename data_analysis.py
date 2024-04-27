import io
import sys

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Check if the data location argument is provided
if len(sys.argv) != 2:
    print("Usage: python data_analysis.py <data_location>")
    sys.exit(1)


# Load the clean dataset
df = pd.read_csv(sys.argv[1])


# Data summary
print("Data Summary:")
summary = df.describe()
data_head = df.head()
print(summary)
print(data_head)


# collecting data info
buffer = io.StringIO()
df.info(buf=buffer)
info = buffer.getvalue()


## Write metrics to file
with open("processed_data/summary.txt", "w") as outfile:
    outfile.write(
        f"\n## Data Summary\n\n{summary}\n\n## Data Info\n\n{info}\n\n## Dataframe\n\n{data_head}"
    )


print("Data summary saved in processed_data folder!")


# Distribution of Happiness Score
plt.figure(figsize=(10, 6))
sns.displot(df["Happiness Score"])
plt.title("Distribution of Happiness Score")
plt.xlabel("Happiness Score")
plt.ylabel("Frequency")
plt.savefig("figures/happiness_score_distribution.png")


# Top 20 countries by Happiness Score
top_20_countries = df.nlargest(20, "Happiness Score")
plt.figure(figsize=(10, 6))
sns.barplot(x="Country", y="Happiness Score", data=top_20_countries)
plt.title("Top 20 Countries by Happiness Score")
plt.xlabel("Country")
plt.ylabel("Happiness Score")
plt.xticks(rotation=90)
plt.savefig("figures/top_20_countries_by_happiness_score.png")


# Scatter plot of Happiness Score vs GDP per Capita
plt.figure(figsize=(10, 6))
sns.scatterplot(x="GDP per Capita", y="Happiness Score", data=df)
plt.title("Happiness Score vs GDP per Capita")
plt.xlabel("GDP per Capita")
plt.ylabel("Happiness Score")
plt.savefig("figures/happiness_score_vs_gdp_per_capita.png")


# Visualize the relationship between Happiness Score and Social Support
plt.figure(figsize=(10, 6))
plt.scatter(x="Social Support", y="Happiness Score", data=df)
plt.xlabel("Social Support")
plt.ylabel("Happiness Score")
plt.title("Relationship between Social Support and Happiness Score")
plt.savefig("figures/social_support_happiness_relationship.png")


# Heatmap of correlations between variables
corr_matrix = df.drop("Country",axis=1).corr()
plt.figure(figsize=(12, 10))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", square=True)
plt.title("Correlation Heatmap")
plt.savefig("figures/correlation_heatmap.png")
print("Visualizations saved to figures folder!")
