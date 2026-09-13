movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

def ratingFunc(movie:list) -> str:

    filteredMovies = []

    for title, year, ratings in movies:

        average = sum(ratings) / len(ratings)

        if average >= 6.0:
            filteredMovies.append((title, year, average))

    filteredMovies.sort(reverse=True)

    for i, (title, year, average) in enumerate(filteredMovies):
        print(f"{i+1}. {title} ({year}) - Average rating: {round(average, 2)} *")
        
ratingFunc(movies)