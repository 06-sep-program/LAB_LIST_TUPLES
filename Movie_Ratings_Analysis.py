movies = [
    ("The Shawshank Redemption", 1994, [9, 10, 10, 9, 8, 9]),
    ("The Godfather", 1972, [10, 9, 8, 10, 9, 7]),
    ("Pulp Fiction", 1994, [9, 8, 7, 8, 6, 5]),
    ("The Dark Knight", 2008, [10, 9, 9, 8, 9, 8]),
    ("Schindler's List", 1993, [8, 9, 9, 7, 6, 8]),
    ("The Room", 2003, [1, 2, 3, 4, 5, 1])
]
ret_list=[]
for titel,year,reting in movies:

   ret_list.append(reting)


#ret_list=[[9, 10, 10, 9, 8, 9], [10, 9, 8, 10, 9, 7], [9, 8, 7, 8, 6, 5], [10, 9, 9, 8, 9, 8], [8, 9, 9, 7, 6, 8], [1, 2, 3, 4, 5, 1]]
avg_list=[]
for i in ret_list:
   ret =round(sum(i)/6,2)
   avg_list.append(ret)

#avg_list= [9.17, 8.83, 7.17, 8.83, 7.83, 2.67]

for i ,m in enumerate(movies):
    avg =avg_list[i]
    if 6<avg:
      titel=m[0] 
      year=m[1]
     
      print (titel,year,avg,"★")

