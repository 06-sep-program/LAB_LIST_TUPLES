movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
movies.sort(key=lambda movie: sum(movie[2]) / len(movie[2]), reverse=True)
for movie in movies:
    title, year, ratings = movie
    average = sum(ratings) / len(ratings)

    if average >= 6.0:
        print(f"{title} ({year}) - Average rating: {average:.2f} ★")