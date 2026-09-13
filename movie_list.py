rating_list= {"movie_1_rating": [9,10,10,9,8,9], "movie_2_rating": [10,9,8,10,9,7], "movie_3_rating": [9,8,7,8,6,5], "movie_4_rating": [10,9,9,8,9,8], "movie_5_rating": [8,9,9,7,6,8], "movie_6_rating": [1,2,3,4,5,1]}

movie_1 = ("The Shawshank Redemption", 
           1994, 
           (sum(rating_list["movie_1_rating"])) / (len(rating_list["movie_1_rating"])))
movie_2 = ("The Godfather", 
           1972, 
           (sum(rating_list["movie_2_rating"])) / (len(rating_list["movie_2_rating"])))
movie_3 = ("Pulp Fiction", 
           1994, 
           (sum(rating_list["movie_3_rating"])) / (len(rating_list["movie_3_rating"])))
movie_4 = ("The Dark Knight", 
           2008, 
           (sum(rating_list["movie_4_rating"])) / (len(rating_list["movie_4_rating"])))
movie_5 = ("Schindler's List", 
           1993, 
           (sum(rating_list["movie_5_rating"])) / (len(rating_list["movie_5_rating"])))   
movie_6 = ("The Room", 
           2003,
           (sum(rating_list["movie_6_rating"])) / (len(rating_list["movie_6_rating"])))


# 1- Display the  movies, along with their title, release year, and average rating.
#print("1.", movie_1[0],"(",movie_1[1],")",(f"{movie_1[2]:.2f}"),"★")
#print("2.", movie_2[0],"(",movie_2[1],")",(f"{movie_2[2]:.2f}"),"★")
#print("3.", movie_3[0],"(",movie_3[1],")",(f"{movie_3[2]:.2f}"),"★")
#print("4.", movie_4[0],"(",movie_4[1],")",(f"{movie_4[2]:.2f}"),"★")
#print("5.", movie_5[0],"(",movie_5[1],")",(f"{movie_5[2]:.2f}"),"★")
#print("6.", movie_6[0],"(",movie_6[1],")",(f"{movie_6[2]:.2f}"),"★")

# 2- Filters out movies with an average rating lower than 6.0.
movies_list = [movie_1, movie_2, movie_3, movie_4, movie_5, movie_6]
movies_list = [movie for movie in movies_list if movie[2] >= 6.00]

# Displays the movies by the order of average rating.
def get_rating(movie):
    return movie[2]
movies_list.sort(key=get_rating, reverse=True)

for number, movie in enumerate(movies_list, 1):
    print(f"{number}. {movie[0]} ({movie[1]}) {movie[2]:.2f} ★")
