def analyze_movie_rating(movie_list):
    """Analyzes movie ratings, filters out low scores, and displays top movies."""
    filterd_movies = []

    for title, year, ratings in movie_list:
        average_rating = round(sum(ratings) / len(ratings), 2)

        if average_rating >= 6.0:
            filterd_movies.append((average_rating, title, year))

    filterd_movies.sort(reverse=True)

    rank = 1 
    for movie in filterd_movies:
        average_rating, title, year = movie
        print(f"{rank}. {title} ({year}) - Avergae rating: {average_rating} ⭐")
        rank += 1


movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

analyze_movie_rating(movies)