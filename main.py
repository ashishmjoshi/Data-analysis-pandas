import pandas as pd
df = pd.read_csv(r'D:\codinggggg\best selling books analysis\bestsellers.csv')
df.drop_duplicates(inplace=True)
df.rename(columns={"Name":"title", "User Rating":"rating"},inplace="True")
print(df.head(10))

author_counts = df['Author'].value_counts()
print(author_counts)
print(df['Genre'].value_counts())
print(df['rating'].value_counts())
print(df['Year'].value_counts())
highest_idx = df['rating'].idxmax()
print("Highest Rated Book:")
print(df.loc[highest_idx])
highest_idx = df['rating'].idxmin()
print("Lowest Rated Book:")
print(df.loc[highest_idx])

avg_rating_by_genre = df.groupby("Genre")["rating"].mean()
print(avg_rating_by_genre)


author_counts.head(10).to_csv("top_authors.csv")
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")

import matplotlib.pyplot as plt
import seaborn as sns

dark_bg = "#1e1b18"        
text_color = "#e6dccf"     
accent = "#a67c52"        
muted = "#6b4f3b"         

plt.style.use("dark_background")
sns.set_theme(style="dark")

plt.rcParams.update({
    "figure.facecolor": dark_bg,
    "axes.facecolor": dark_bg,
    "axes.edgecolor": text_color,
    "axes.labelcolor": text_color,
    "xtick.color": text_color,
    "ytick.color": text_color,
    "text.color": text_color,
    "font.family": "serif",
    "font.size": 11
})

top_authors = df['Author'].value_counts().head(10)

plt.figure(figsize=(10,6))
sns.barplot(
    x=top_authors.values,
    y=top_authors.index,
    color=accent
)

plt.title("The Authors Who Reign Over the Bestseller Lists", fontsize=14)
plt.xlabel("Number of Bestselling Works")
plt.ylabel("Author")

plt.tight_layout()
plt.savefig("top_authors_dark.png", dpi=300)
plt.show()

plt.figure(figsize=(8,5))
sns.histplot(
    df['rating'],
    bins=10,
    kde=True,
    color=muted
)

plt.title("A Study of Bestseller Ratings", fontsize=14)
plt.xlabel("Rating")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("rating_distribution_dark.png", dpi=300)
plt.show()

avg_rating = df.groupby("Genre")["rating"].mean()

plt.figure(figsize=(6,4))
sns.barplot(
    x=avg_rating.index,
    y=avg_rating.values,
    palette=[accent, muted]
)

plt.title("Average Rating Across Literary Realms", fontsize=14)
plt.xlabel("Genre")
plt.ylabel("Average Rating")

plt.tight_layout()
plt.savefig("genre_rating_dark.png", dpi=300)
plt.show()

year_counts = df['Year'].value_counts().sort_index()

plt.figure(figsize=(10,5))
sns.lineplot(
    x=year_counts.index,
    y=year_counts.values,
    color=accent,
    linewidth=2.5
)

plt.title("Chronicles of Bestseller Publication", fontsize=14)
plt.xlabel("Year")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig("books_per_year_dark.png", dpi=300)
plt.show()
