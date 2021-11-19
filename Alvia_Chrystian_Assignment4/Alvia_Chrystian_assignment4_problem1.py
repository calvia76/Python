#Weight Loss Log with Sentinals
print("\nEnter '-1' when you wish to end the program\n")
flag = -1
grade = 0
num = 0
total = 0

i=0
wArray = []
while grade != flag:
    num+=1
    grade = int(input("Enter your weight on day " + str(num) + ":"))
    
    if(grade == flag):
        
        num -= 1
        avg = total/(num)

        wlTotal = wArray[0]-wArray[num-1]
        
        print("\nAverage Weight over ",num, " days: " , avg)
        print("Total Weight Loss over ", num, " days: ", wlTotal )
        break
    wArray.insert(i,grade)
    i+=1
    total += grade
    
        
