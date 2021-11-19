
#60s = 1min
#3600s = 1 hour

print("\nEnter a negative integer value when you would like to quit the program\n")
counter = 0
while(True):
    hourStr = " hour"
    minStr = " minute"
    secStr = " second"

    hours = 0
    minutes = 0
    seconds = 0
    
    time = int(input("Please enter the number of second(s) elapsed: "))
    if(time < 0):
        print("Exiting program...")
        break
    
    for x in range(0,time):
        counter+=1
        if(counter == 3600):
            time = time-counter
            hours+=1
            counter=0
            continue
        if(time < 3600 and counter == 60):
            time = time-counter
            minutes +=1
            counter = 0
            continue
        if(time < 60):
            seconds = time
            break
    if(hours > 1 or hours == 0):
        hourStr = hourStr+"s"
    if(minutes > 1 or minutes == 0):
        minStr = minStr+"s"
    if(seconds > 1 or seconds == 0):
        secStr = secStr+"s"
    print(str(hours) + hourStr +", " + str(minutes) + minStr +", " + str(seconds) + secStr)
