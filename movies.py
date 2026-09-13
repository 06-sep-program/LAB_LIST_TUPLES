print ("----- List of movies -----")
print() # new line

movies = [
    # (movie title , release year , list of rating)
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]

# Print the list of movies  WITHOUT sorting
counter = 1

for movie in movies:
    movieTitle = movie[0]
    releaseYear = movie[1]
    listOfRating = movie[2]


    rating_average = round (sum(listOfRating) / len(listOfRating) , 2)

    if rating_average >= 6.0:
        
        print(counter , "." , movieTitle , (releaseYear) , " - " , "Average rating: " , rating_average , "★")
        counter += 1

# ----------------------------------------------------

# Print the list of movies  WITH sorting
print ("----- List of movies based on ratings -----")
print() # new line

movies_with_sorting = [] # create empty list

for movie in movies:
    movieTitle = movie[0]
    releaseYear = movie[1]
    listOfRating = movie[2]

    rating_average = round (sum(listOfRating) / len(listOfRating) , 2)

    if rating_average >= 6.0:
        movies_with_sorting.append(
             (movieTitle , releaseYear , rating_average) 
             ) 

movies_with_sorting.sort(key = lambda movie: movie[2] , reverse = True) # Descending order

counter = 1

for movie in movies_with_sorting:
    print(counter , "." , movie[0] , movie[1] , " - " , "Average rating: " , movie[2] , "★")
    counter += 1