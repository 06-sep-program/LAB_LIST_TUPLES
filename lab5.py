movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
filteredMovies= []
for title, year, rating in movies:
    avg = sum(rating)/len(rating)
    if avg >= 6.0:
        filteredMovies.append((title,year,avg))

filteredMovies.sort(key=lambda movie: movie[2], reverse=True)

for index, (title, year, avg) in enumerate(filteredMovies, start=1):

    print(f"{index}. {title} ({year}) – Avergae rating: {avg:.2f} ★")
