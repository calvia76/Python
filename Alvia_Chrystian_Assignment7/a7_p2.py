import time

movie_reviews = open("movie_reviews.txt","r")
file = movie_reviews.read()

#evaluates string input to pick apart words and add them to the dictionary
words = {}
def word_eval(string):
    temp = ""
    score = 0
    for x in string:
        if(x.isnumeric()):
            score = x
            continue
        if(x == " "):
            words[temp] = (score+=score, count+=count
        temp+=x

temp = ""
review = ""
count = 0
i=0
val = 0
for x in file:
    if(x.isnumeric() and len(review)!=0):
        if(evaluation(keyword.lower(),review)):
            val += int(review[0])
            review = ""
            continue
        else:
            review = x
            continue
    else:
        review += x.lower()
        continue
        
