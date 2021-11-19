import random

dieArray = [4, 6, 8, 10, 12, 20]
counter = 0
doubles = 0
checker = 0

flag1 = " "
flag2 = " "


while(flag1):
    die = int(input("How many sides on your dice? (4, 6, 8, 10, 12, or 20?) "))
    for x in dieArray:
        checker +=1
        if(die == x):
            print("\nThanks! Here we go ...\n")
            flag1 = False
            break 
        elif((checker == len(dieArray))):
            print("Sorry, that's not a valid size")
            checker = 0
            continue
        else:
            continue
            
if(die == 4):
    while(flag2):
        die1 = random.randint(1,4)
        die2 = random.randint(1,4)
        counter += 1
        if(die1 == die2):
            doubles += 1
        print(str(counter)+". die number 1 is: ", die1, "and die number 2 is: " ,die2)
        if(die1 == 1 and die2 == 1):
            doubpercent = (doubles/counter)*100
            
            print("\nYou rolled snake eyes on try number " + str(counter)+"!")
            print("Along the way you rolled doubles "+str(doubles) +" time(s) (" + str(format(doubpercent,"0.2f"))+ "% of all rolls were doubles)")
            
            flag2 = False
                        
        else:
            continue
        
if(die == 6):
    while(flag2):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        counter += 1
        if(die1 == die2):
            doubles += 1
        print(str(counter)+". die number 1 is: ", die1, "and die number 2 is: " ,die2)
        if(die1 == 1 and die2 == 1):
            doubpercent = (doubles/counter)*100
            
            print("\nYou rolled snake eyes on try number " + str(counter)+"!")
            print("Along the way you rolled doubles "+str(doubles) +" time(s) (" + str(format(doubpercent,"0.2f"))+ "% of all rolls were doubles)")
            
            flag2 = False
                        
        else:
            continue

if(die == 8):
    while(flag2):
        die1 = random.randint(1,8)
        die2 = random.randint(1,8)
        counter += 1
        if(die1 == die2):
            doubles += 1
        print(str(counter)+". die number 1 is: ", die1, "and die number 2 is: " ,die2)
        if(die1 == 1 and die2 == 1):
            doubpercent = (doubles/counter)*100
            
            print("\nYou rolled snake eyes on try number " + str(counter)+"!")
            print("Along the way you rolled doubles "+str(doubles) +" time(s) (" + str(format(doubpercent,"0.2f"))+ "% of all rolls were doubles)")
            
            flag2 = False
                        
        else:
            continue

if(die == 10):
    while(flag2):
        die1 = random.randint(1,10)
        die2 = random.randint(1,10)
        counter += 1
        if(die1 == die2):
            doubles += 1
        print(str(counter)+". die number 1 is: ", die1, "and die number 2 is: " ,die2)
        if(die1 == 1 and die2 == 1):
            doubpercent = (doubles/counter)*100
            
            print("\nYou rolled snake eyes on try number " + str(counter)+"!")
            print("Along the way you rolled doubles "+str(doubles) +" time(s) (" + str(format(doubpercent,"0.2f"))+ "% of all rolls were doubles)")
            
            flag2 = False
                        
        else:
            continue

if(die == 12):
    while(flag2):
        die1 = random.randint(1,12)
        die2 = random.randint(1,12)
        counter += 1
        if(die1 == die2):
            doubles += 1
        print(str(counter)+". die number 1 is: ", die1, "and die number 2 is: " ,die2)
        if(die1 == 1 and die2 == 1):
            doubpercent = (doubles/counter)*100
            
            print("\nYou rolled snake eyes on try number " + str(counter)+"!")
            print("Along the way you rolled doubles "+str(doubles) +" time(s) (" + str(format(doubpercent,"0.2f"))+ "% of all rolls were doubles)")
            
            flag2 = False
                        
        else:
            continue

if(die == 20):
    while(flag2):
        die1 = random.randint(1,20)
        die2 = random.randint(1,20)
        counter += 1
        if(die1 == die2):
            doubles += 1
        print(str(counter)+". die number 1 is: ", die1, "and die number 2 is: " ,die2)
        if(die1 == 1 and die2 == 1):
            doubpercent = (doubles/counter)*100
            
            print("\nYou rolled snake eyes on try number " + str(counter)+"!")
            print("Along the way you rolled doubles "+str(doubles) +" time(s) (" + str(format(doubpercent,"0.2f"))+ "% of all rolls were doubles)")
            
            flag2 = False
                        
        else:
            continue
    
                        
                    
