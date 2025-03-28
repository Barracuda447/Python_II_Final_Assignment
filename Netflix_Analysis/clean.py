import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
FILE = r"Netflix_Analysis\netflix_titles.csv"
df = pd.read_csv(FILE)

#Check for missing values
missingValues = df.isnull().sum()
print(f"There is {missingValues.sum()} missing values.")

#Drop rows with missing date_added
df = df.dropna(subset=['date_added'])

#Fill missing values in categorial columns
catCol = df.select_dtypes(include=['object']).columns
df[catCol] = df[catCol].fillna("Missing Value")

#Check for missing values again
missingValues = df.isnull().sum()
print(f"There is {missingValues.sum()} missing values.")

#Find count of unique values in each column
for col in df.columns:
    uniqueValues = df[col].nunique()
    print(f"Column {col} has {uniqueValues} unique values.")



#Find most frequent type
    # frequentType = df['type'].mode()[0]
    # print(f"Most frequent type is {frequentType}")
moviesdf = df[df['type']=='Movie']
movieType = moviesdf['listed_in'].str.split(',').explode().str.strip()
mostFrequent = movieType.mode()
print(f"Most common type of movie is: {mostFrequent.iloc[0]}")

#Find oldest and newest movie
oldestYear = df.loc[df['type']=="Movie", 'release_year'].min()
oldestMovies = df[(df['release_year']==oldestYear)& (df['type']=="Movie")]
print(f"Oldest movie(s):")
print("\n".join(oldestMovies['title'].tolist()))
newestYear = df.loc[df['type']=="Movie", 'release_year'].max()
newestMovies = df[(df['release_year']==newestYear)&(df['type']=="Movie")]
print()
print()
print("Newest Movie(s)")
print("\n".join(newestMovies['title'].tolist()))
#Find year with most releases
years = df['release_year'].value_counts()
mostYear = years.idxmax()
print(f"Year with most titles released: {mostYear}")

df.to_csv(r"Netflix_Analysis\cleaned_data.csv")


#ASK TEACHER ABOUT OLDEST/NEWEST MOVIE AND FREQUENT TYPE


