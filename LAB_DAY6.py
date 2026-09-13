Shawshank_Redemption:list = [9,10,10,9,8,9]
God_Father:list = [10,9,8,10,9,7]
pulp_fiction:list = [9, 8, 7, 8, 6, 5]
The_Dark_Knight:list = [10, 9, 9, 8, 9, 8]
Schindlers_List:list = [8, 9, 9, 7, 6, 8]
The_Room:list =  [1, 2, 3, 4, 5, 1]




''' this functions calculate the average'''
av1 = sum(Shawshank_Redemption) / len(Shawshank_Redemption)
av2 = sum(God_Father) / len(God_Father)
av3 = sum(pulp_fiction)/ len(pulp_fiction)
av4 = sum(The_Dark_Knight) / len(The_Dark_Knight)
av5 = sum(Schindlers_List) / len(Schindlers_List)
av6= sum(The_Room) / len(The_Room)


movies = [
    ("The Shawshank Redemption", 1994,  av1),
    ("The Godfather", 1972, av2),
    ("Pulp Fiction", 1994, av3),
    ("The Dark Knight", 2008, av4),
    ("Schindler's List", 1993, av5),
    ("The Room", 2003, av6)
]

for rating_acending in movies:
   rating_acending[2] >= 9
   print("{} ({}) - Average Rating: {:.2f} ★".format( 
            rating_acending[0],
            rating_acending[1],
            rating_acending[2]    ))

else:
    print("{} ({}) - Average Rating: {:.2f} ★".format(
            rating_acending[0],
            rating_acending[1],
            rating_acending[2] ))
