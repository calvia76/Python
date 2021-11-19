movie_reviews = open("movie_reviews.txt","r")

file = movie_reviews.read()


def evaluation(keyword,string):
    if keyword in string:
        return True
    else:
        return False

keyword = input("Enter a word to test: ")

review = ""
count = 0

val = 0
for x in file:
    if(x.isnumeric() and len(review)!=0):
        if(evaluation(keyword.lower(),review)):
            val += int(review[0])
            count+=1
            review = ""
            continue
        else:
            review = x
            continue
    else:
        review += x.lower()
        continue
    

keyword = "'" + keyword + "'" 
print(keyword + " appears ",count, " times")
if(count == 0):
    print("There is no average score for reviews containing the word " + keyword)
    print("Cannot determine if this word is positive or negative")
else:
    score = val/count
    print("The average score for reviews containing the word " + keyword + " is ", score)
    if(score < 2):
        print("This is a negative word")
    if(score >= 2):
        print("This is a positive word")










