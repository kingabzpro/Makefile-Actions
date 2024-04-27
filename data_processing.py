import pandas as pd


# Load the dataset
df = pd.read_csv("raw_data\WHR2023.csv")


# Rename columns to more descriptive names
df.columns = [
    "Country",
    "Happiness Score",
    "Happiness Score Error",
    "Upper Whisker",
    "Lower Whisker",
    "GDP per Capita",
    "Social Support",
    "Healthy Life Expectancy",
    "Freedom to Make Life Choices",
    "Generosity",
    "Perceptions of Corruption",
    "Dystopia Happiness Score",
    "GDP per Capita",
    "Social Support",
    "Healthy Life Expectancy",
    "Freedom to Make Life Choices",
    "Generosity",
    "Perceptions of Corruption",
    "Dystopia Residual",
]


# Handle missing values by replacing with mean
df.fillna(df.mean(numeric_only=True), inplace=True)


# Check for missing values after cleaning
print("Missing values after cleaning:")
print(df.isnull().sum())




print(df.head())


# Save the cleaned and normalized dataset to a new CSV file
df.to_csv("processed_data\WHR2023_cleaned.csv", index=False)