#SEQUENCING
while(True):
    x = int(input("Enter a positive integer: "))
    if( x == 0):
        print("Exiting program...")
        break
    elif(x < 0):
        continue
    else:
        break


count = 0
temp1 = 0

first = 0
fcount = 0

second = 0
scount = 0
while(x!=1):
    if(x%2==0):
        x = x/2
        count+=1
        continue
    else:
        x = (x*3)+1
        #Couldn't figure it out:
        
        #if(count == 0):
        #    first = x
        #if(count > 0):
        #    second = x
        #   if(first > second):
        #        continue
        #   else:
        #        first = second
        #        second = 0
        #        continue
        count+=1
        continue
print("It took the sequence " + str(count) + " steps to reach 1")




#BONUS QUESTION
#My favorite was question 3 because it was the most challenging

#question 1 took me about 30 minutes to figure out, my brain couldn't figure out the sequence
#question 2 took me 5 minutes because I already had it implemented from a homework assignment
#question 3 took me the remaining time to figure out how to find the biggest/second biggest number in the sequence

    
        
