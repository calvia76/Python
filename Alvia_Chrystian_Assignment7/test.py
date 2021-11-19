movie_reviews = open("movie_reviews.txt","r")

file = movie_reviews.read()


string = "1 I am feeling quite happy and hungry and yeetish"
keyword = "and"
i=0
x = file.count(keyword)
print(x)
