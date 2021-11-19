date = int(input("Enter a date in YYYYMMDD format (i.e. 20200903 for September 3rd, 2020): "))

sept = [3,5,8,10,15,17,22,24,29]
octo = [1,6,8,13,15,20,22,27,29]
nov = [3,5,10,12,17,19,24]
dec = [1,3,8,10]

if((len(str(date)) != 8)):
    print("That's not a valid date!")
    exit()

dTemp = date
dateD = dTemp % 100
dTemp = (dTemp - dateD)/100
dateM = dTemp % 100
dTemp = (dTemp - dateM)/100
dateY = dTemp

if(((dateM == 9) and dateD < 2) or (0 < dateM < 8) and dateY < 2020):
    print("This date is before the semester begins")
    exit()
if((dateM == 12 and dateD > 20) or dateY > 2020):
    print("This date is after the semester ends")
    exit()
if((1 < dateM > 12) or (1 < dateD > 31) or(dateM == 3 and dateD > 28)
   or ((dateM == 7 or dateM == 4 or dateM == 6 or dateM == 11) and dateD > 30)):
    print("That's not a valid date!")
    exit()
    
print("Today's date is ",int(dateM),"/",int(dateD),"/",int(dateY))

if(dateM == 9):
    for x in sept:
        if(dateD == x):
            print("You have class today")
            break
        else:
            print("You don't have class today")
            break
if(dateM == 10):
    for x in octo:
        if(dateD == x):
            print("You have class today")
            break
        else:
            print("You don't have class today")
            break
if(dateM == 11):
    for x in nov:
        if(dateD == x):
            print("You have class today")
            break
        else:
            print("You don't have class today")
            break
if(dateM == 12):
    for x in dec:
        if(dateD == x):
            print("You have class today")
            break
        else:
            print("You don't have class today")
            break


