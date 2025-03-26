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
oldestMovie = df[df['release_year'] == df['release_year'].min()]
newestMovie = df[df['release_year'] == df['release_year'].max()]

#Find average release year
avgYear = df['release_year'].mean()
print(f"Average release year of movies is: {int(avgYear)}")

df.to_csv(r"Netflix_Analysis\cleaned_data.csv")


#ASK TEACHER ABOUT OLDEST/NEWEST MOVIE AND FREQUENT TYPE


