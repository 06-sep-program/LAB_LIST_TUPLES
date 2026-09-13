movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

point = 0
for movie in movies:
    total = 0
    plus = movie[-1]
    total = sum(plus)
    number = len(plus)
    average = total/number
    if average > 6 :
        point = point + 1
        print(f"{point}. {movie[0]} ({movie[1]}) - Avergae rating: {round(average , 2)} ★")
    


    