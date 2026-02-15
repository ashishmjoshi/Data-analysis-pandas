import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(script_dir, 'bestsellers.csv'))

df.drop_duplicates(inplace=True)


df.rename(columns={"Name": "Title", "User Rating": "Rating"}, inplace=True)

df["Price"]= df["Price"].astype(float)

author_counts = df['Author'].value_counts()
print(author_counts)
print("\n")
print(df["Genre"].value_counts())
print(df["Rating"].value_counts())

avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

# Export top selling authors to a CSV file
author_counts.head(10).to_csv("top_authors.csv")

# Export average rating by genre to a CSV file
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")