
left = False
right = False

while(True):
    x = int(input("\nHow many columns? (Enter a positive integer) "))
    if(x<0):
        print("\n---------- INVALID ENTRY: Enter a positive integer ----------")
        continue
    elif(x==0):
        print("\n---------- INVALID ENTRY: Enter a number above 0 ---------- ")
        continue
    else:
        break
while(True):
    lr = input("\nWhich direction should the arrow face?\n(Enter 'L' or 'left' for left facing and 'R' or 'right' for right facing) ")
    if( lr.lower()== "left" or lr.lower() == "l"):
        left = True
    elif(lr.lower() == "right" or lr.lower() == "r"):
        right = True
    else:
        print("\n------------- INVALID DIRECTION ENTRY: Try again -------------")
        continue
   
    break

    
if(bool(right)):
    for i in range(1,x+1):
        for j in range(0,i):
            print(" ", end="")
        for k in range(j,i):
            print("*",end="")
        print()

    while(k>0):
        for m in range(1,k+1):
            print(" ",end="")
        for n in range(0,1):
            print("*",end="")
        k-=1
        print()
        
if(bool(left)):
    temp = x
    while(temp>0):
        for m in range(1,temp):
            print(" ",end="")
        for n in range(0,1):
            print("*",end="")
        print()
        temp-=1
    for i in range(1,x):
        for j in range(0,i):
            print(" ", end="")
        for k in range(j,i):
            print("*",end="")
        print()

    
