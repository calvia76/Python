print("\n\t Pokemon Distance Calculator\n---------------------------------------------\n")
name1 = input("1. Enter the name of the first Pokemon: ")

x1 = float(input("2. Enter the x coordinate of the first Pokemon: "))
y1 = float(input("3. Enter the y coordinate of the first Pokemon: "))

name2 = input("4. Enter the name of the second Pokemon: ")

x2 = float(input("5. Enter the x coordinate of the second Pokemon: "))
y2 = float(input("6. Enter the y coordiante of the second Pokemon: "))
print("\n")
dist = ((x2-x1)**2 + (y2-y1)**2)**.05
print("\tThe distance between " , name1 , " and " , name2 , " is ", format(dist,"0.2f") , " inches.")

