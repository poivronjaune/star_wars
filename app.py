import pandas as pd

def load_movies():
    df = pd.read_json("raw_data/movies.json", orient="records")
    return df

movies = load_movies()
print(movies)
