import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
FILE = r"Netflix_Analysis\cleaned_data.csv"
df = pd.read_csv(FILE)

#10 countries with highest number of titles
top10countries = df['country'].value_counts().head(10)
plt.figure(figsize=(10,5))
plt.bar(top10countries.index, top10countries.values)
plt.title("Top 10 Countries with the most titles")
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation=45)
plt.subplots_adjust(bottom=0.3)
plt.show()

#10 top directors
df_directors = df.assign(director=df['director'].str.split(',')).explode('director')
df_directors['director'] = df_directors['director'].str.strip()
df_directors = df_directors[df_directors['director'] != "Missing Value"]
top10directors = df_directors['director'].value_counts().head(10)
plt.figure(figsize=(10,5))
plt.bar(top10directors.index, top10directors.values)
plt.title("Top 10 Directors")
plt.xlabel("Director")
plt.ylabel("Number of Releases")
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.3)
plt.show()

#  # of Netflix titles by release year
plt.figure(figsize=(10,5))
plt.hist(df['release_year'], bins=80)
plt.title("Distrubution of Netflix Titles by Release Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.grid(axis="y", linestyle='--')
plt.show()
