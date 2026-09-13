movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

movie_ratings = []

for movie in movies:
    title, release_year, ratings = movie
    if ratings:
        movie_rating= sum(ratings) / (len(ratings))
        if movie_rating >= 6:
            movie_ratings.append((movie_rating, title, release_year))

movie_ratings.sort(key=lambda movie: -movie[0])
for order, (movie_rating, title, release_year) in enumerate(movie_ratings, start=1):
    print(f"{order}. {title} ({release_year}) - Average Rating: {movie_rating:.2f} ★")       

