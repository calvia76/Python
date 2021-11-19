def differ_by_one(str1, str2):
    i = 0
    for x in str1:
        if(x in str2):
            i+=1
        else:
            continue
    if(i >= len(str1)-1):
        return True
    else:
        return False


valid = []
print("Welcome to word ladder!")
initial = input("Please enter the initial word: ")
goal = input("Please enter the goal word: ")
print("Asking for valid words...")
valid.append(initial)
valid.append(goal)


while(True):
    valid_words = input("Please enter a valid word: ")
    if(valid_words == " "):
        break
    valid.append(valid_words)
    
print("Beginning game...")
print("Current word is " + initial)

atttempts = 0
attempts = len(valid)

while(True):
    if(attempts == 0):
        print("Game over!")
        quit()
    print("You have " +str(attempts) + " attempt(s) to get the goal word.")
    
    word = input("Please enter next word: ")
    i = 0
    counter = 0
    while(i != len(valid)):
        if(word == goal):
            print("Victory!")
            quit()
        if(differ_by_one(valid[i],word)):
            counter+=1
            i+=1
            continue
        else:
            i+=1
            continue
    if(counter>1):
        print("That is a valid word!")
        attempts-=1
    else:
        print("Sorry, that is not a valid word")
        attempts-=1






    
