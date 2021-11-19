
print("--------------------------------------------------------------------------\n\t\tINSTRUCTIONS\nEnter the start date and birthdate for an employee\nto determine their age tat the start of employment\n")
start = int(input("Enter start date MMDDYYYY: "))
birth = int(input("\nEnter birth date MMDDYYYY: "))

print("\n--------------------------------------------------------------------------")

#Math to split up MM DD YYYY
startY = start % 10000
start = (start - startY)/10000
startD = start % 100
startM = (start - startD)/100

    
if(startM == 1):
    sMonth = "January"
if(startM == 2):
    sMonth = "Febuary"
if(startM == 3):
    sMonth = "March"
if(startM == 4):
    sMonth = "April"
if(startM == 5):
    sMonth = "May"
if(startM == 6):
    sMonth = "June"
if(startM == 7):
    sMonth = "July"
if(startM == 8):
    sMonth = "Agust"
if(startM == 9):
    sMonth = "September"
if(startM == 10):
    sMonth = "October"
if(startM == 11):
    sMonth = "November"
if(startM == 12):
    sMonth = "December"

#adding appropriate ending to day of date
if(startD == 1 or startD == 21 or startD == 31):
    str_startD = str(int(startD))+ "st"
elif(startD == 2 or startD == 22):
    str_startD = str(int(startD))+ "nd"
else:
    str_startD = str(int(startD))+ "th"
    
print("The start date is ", sMonth," ", str_startD,", ",startY)


birthY = birth % 10000
birth = (birth - birthY)/10000
birthD = birth % 100
birthM = (birth - birthD)/100

    
if(birthM == 1):
    bMonth = "January"
if(birthM == 2):
    bMonth = "Febuary"
if(birthM == 3):
    bMonth = "March"
if(birthM == 4):
    bMonth = "April"
if(birthM == 5):
    bMonth = "May"
if(birthM == 6):
    bMonth = "June"
if(birthM == 7):
    bMonth = "July"
if(birthM == 8):
    bMonth = "Agust"
if(birthM == 9):
    bMonth = "September"
if(birthM == 10):
    bMonth = "October"
if(birthM == 11):
    bMonth = "November"
if(birthM == 12):
    bMonth = "December"

if(birthD == 1 or birthD == 21 or birthD == 31):
    str_birthD = str(int(birthD))+ "st"
elif(birthD == 2 or birthD == 22):
    str_birthD = str(int(birthD)) + "nd"
else:
    str_birthD = str(int(birthD)) + "th"
print("\nThe contestant was born on ", bMonth," ", str_birthD,", ",birthY)

#determining whether the contestant will be/is of age to participate
ageY = int(startY) - int(birthY)
mDiff = int(startM) - int(birthM)
dDiff = int(startD) - int(birthD)
if(ageY < 21 or mDiff < 0):
    print("\nNOT ELIGIBLE: The contestant won't be 21 by the time taping begins.")
elif(mDiff == 0):
    if(dDiff > 0):
        print("\nNOT ELIGIBLE: The contestant won't be 21 by the time taping begins.")
    else:
        print("\nELIGIBLE: The contestant will be 21 by the time taping begins.")
else:
    print("\nELIGIBLE: The contestant will be 21 by the time taping begins.")
    


