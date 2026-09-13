movies = []

movies.append(("Inception", 2010, [8, 9, 9, 8]))
movies.append(("The Dark Knight", 2008, [9, 9, 10, 9]))
movies.append(("Interstellar", 2014, [8, 8, 9, 10]))
movies.append(("The Room", 2003, [3, 4, 2, 5]))
movies.append(("The Matrix", 1999, [9, 8, 9, 10]))


def classify_rating(rating):
    """
    Classifies a movie based on its average rating.
    """
    if rating >= 9.0:
        return "Excellent"
    elif rating >= 8.0:
        return "Very Good"
    elif rating >= 6.0:
        return "Good"
    else:
        return "Poor"


results = []

for movie in movies:
    title, year, ratings = movie
    average_rating = sum(ratings) / len(ratings)

    if average_rating >= 6.0:
        results.append((title, year, average_rating))


results.sort(key=lambda movie: movie[2], reverse=True)


print("\nMovies with rating 6.0 or higher:")

for title, year, average_rating in results:
    rating_level = classify_rating(average_rating)
    print(
        f"{title} ({year}) - Average rating: "
        f"{average_rating:.2f} ★ - {rating_level}"
    )