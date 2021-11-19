while(True):
    students = int(input("How many students are in your class? "))
    if(students < 0):
        print("Invalid entry, try again.")
        continue
    else:
        break

while(True):
    tInput = int(input("How many tests are in this class? "))
    if(tInput < 0):
        print("Invalid entry, try again.")
        continue
    else:
        print("\nHere we go!\n")
        break
i = 1

total = 0
while(i < students+1):
    tests = tInput
    j=1
    print("**** Student #" + str(i) +"****")
    while(j <= tests):
        score = float(input("Enter score for test #"+str(j)+": "))
        if(score < 0):
            print("Invalid score, try again")
            continue
        else:
            total += score
            j+=1
            if(j > tests):
                avg = total/tests
                print("Average score for student #"+str(i)+" is "+str(avg)+"\n")
                avg=0
                total=0
            #print("total: " +str(total) + "j: " + str(j))
            
    i+=1
        
