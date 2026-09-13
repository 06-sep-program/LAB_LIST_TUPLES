movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
if __name__ == "__main__":
    for title, year, ratings in movies:
        average_rating = sum(ratings) / len(ratings)
        print(f"{title} ({year}) - Avg: {average_rating:.2f}")

# Filter out movies with an average rating below 6.0
filtered_movies = [(title, year, ratings) for title, year, ratings in movies if sum(ratings) / len(ratings) >= 6.0]
print("\nFiltered Movies (Avg >= 6.0):")
filtered_movies = sorted(
    filtered_movies,
    key=lambda movie: sum(movie[2]) / len(movie[2]),
    reverse=True
)

for title, year, ratings in filtered_movies:
    average_rating = sum(ratings) / len(ratings)
    print(f"{title} ({year}) - Avg: {average_rating:.2f}""*""")

user_input = input("\nEnter a movie title to search: ")

if user_input:
    found_movies = [
        (title, year, ratings)
        for title, year, ratings in movies
        if user_input.lower() in title.lower()
    ]

    if found_movies:
        print("\nSearch Results:")
        for title, year, ratings in found_movies:
            average_rating = sum(ratings) / len(ratings)
            print(f"{title} ({year}) - Avg: {average_rating:.2f}")
    else:
        print("No movies found with that title.")