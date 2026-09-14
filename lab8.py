movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

good_movies = []

for title, year, ratings in movies:
    avg = sum(ratings) / len(ratings)

    if avg >= 6.0:
        good_movies.append((title, year, avg))

good_movies.sort(key=lambda x: x[2], reverse=True)

for i, (title, year, avg) in enumerate(good_movies, start=1):
    print(f"{i}. {title} ({year}) - Average rating: {avg:.2f} ★")
