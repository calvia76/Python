import math
x1 = float(input("Enter first x coordinate: "))
y1 = float(input("Enter first y coordinate: "))

x2 = float(input("Enter second x coordinate: "))
y2 = float(input("Enter second y coordiante: "))

x3 = float(input("Enter third x coordinate: "))
y3 = float(input("Enter third y coordinate: "))

side1 = format(math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2),2)),".2f")
side2 = format(math.sqrt(math.pow((x1 - x3),2) + math.pow((y1 - y3),2)),".2f")
side3 = format(math.sqrt(math.pow((x2 - x3),2) + math.pow((y2 - y3),2)),".2f")

print("\nSide 1: ",side1,"\nSide 2: ",side2,"\nSide 3: ",side3)

if((side1 > side2) and (side2>side3)
   and(side2>side3) and (side3 > side1)
    and(side3>side2) and (side1 > side2)):
    print("\nthis is a valid triangle")
    
    if((side1 != side3) and (side1 != side2) and (side2 != side3)):
        print("\nThis is a Scalene Triangle")
    
    if(((side1 != side2) and (side1 == side3) and (side2 == side3))
      or ((side1 == side2) and (side1 != side3) and (side2 == side3))
      or ((side1 == side2) and (side1 == side3) and (side2 != side3))):
         print("\nThis is an Isosceles Triangle")

elif((side1 == side3) and (side1 == side2) and (side2 == side3)):
    print("\nThis is a valid Triangle")
    print("\nThis is an Equilateral Triangle")
else:
    print("\nThis is not a valid triangle")
    


    
    
   
