import random
import time
import math



miss = 0

redRect = 0
greenRect = 0
blueCirc = 0
dgreyCirc = 0
lgreyCirc = 0


while(True):
    throws = int(input("Number of throws: "))
    if(throws < 0):
        print("INVALID ENTRY: Enter a positive integer")
        continue
    elif(throws == 0):
        print("INVALID ENTRY: You have to throw something, don't be chicken.")
        continue
    else:
        break
    
start_time = time.time()
counter = throws
while(counter > 0):
    dartX = random.uniform(0,800)
    dartY = random.uniform(0,500)
    counter-=1
   
    #Red rectangle
    if((350 < dartX < 450) and (300 < dartY < 450)):
        redRect += 1
        continue
        
    #Green rectangle
    if((550 < dartX < 750) and (50 < dartY < 450)):
        if((600 < dartX < 700) and (100 < dartY < 200)):
            miss+=1
            continue
        elif((600 < dartX < 650) and (250 < dartY < 300)):
            miss+=1
            continue
        elif((650 < dartX < 700) and (350 < dartY < 400)):
            miss+=1
            continue
        else:
            greenRect+=1
            continue

    #Blue circle
    if((300 < dartX < 500) and (50 < dartY < 250)):
        dist = math.sqrt(math.pow(dartX-400,2)+math.pow(dartY-150,2))
        if(dist <= 100):
            blueCirc+=1
            dist = 0
            continue
        else:
            dist = 0
            miss+=1
            continue
    #Dark Grey Cricles
            #This block accounts for the top section of the smaller circle only
    if((100 < dartX < 200) and (150 < dartY < 200)):
        dist = math.sqrt(math.pow(dartX-150,2) + math.pow(dartY-200,2))
        if(dist <= 50):
            dgreyCirc+=1
            dist=0
            continue
        else:
            dist = 0
            miss+=1
            continue
        #This block will account for the larger circle, without the intersecting light grey area, broken
        #into 3 quadrants
    #Q1
    if((50 < dartX < 100) and (200 < dartY < 400)):
        dist = math.sqrt(math.pow(dartX-150,2) + math.pow(dartY-300,2))
        if(dist <= 100):
            dgreyCirc+=1
            dist=0
            continue
        else:
            dist = 0
            miss+=1
            continue
    #Q2
    if((100 < dartX < 200) and (250 < dartY < 400)):
        dist = math.sqrt(math.pow(dartX-150,2) + math.pow(dartY-300,2))
        if(dist <= 100):
            dgreyCirc+=1
            dist = 0
            continue
        else:
            dist = 0
            miss+=1
            continue
    #Q3
    if((200 < dartX < 250) and (200 < dartY < 400)):
        dist = math.sqrt(math.pow(dartX-150,2) + math.pow(dartY-300,2))
        if(dist<=100):
            dgreyCirc+=1
            dist=0
            continue
        else:
            dist = 0
            miss+=1
            continue
        
    #Light Grey Intersection of Circles
    if((100 < dartX < 200) and (200 < dartY < 250)):
        #Distance relative to larger circle's center to point of dart's position inside light grey area
        dist1 = math.sqrt(math.pow(dartX-150,2) + math.pow(dartY-300,2))
        #Distance relative to smaller circle's center to point of dart's position inside light grey area
        dist2 = math.sqrt(math.pow(dartX-150,2) + math.pow(dartY-200,2))
        #if the distance from largest circle is within 100 and also is within 50 of the smaller circle,
        #the dart is within the grey area
        if(dist1 <= 100 and dist2 <=  50):
            lgreyCirc+=1
            dist1 = 0
            dist2 = 0
            continue
        #Otherwise, it is outside of the area of the light grey intersection and is dark grey
        else:
            dgreyCirc+=1
            dist1 = 0
            dist2 = 0
            continue
    else:
        miss+=1
        continue
#-------------------------------- end while ------------------

num = [redRect, blueCirc, greenRect, dgreyCirc, lgreyCirc, miss]

#to check array values before string manipulation
#for x in num:
#    print(x)

i=0
#convert int to string and add commas where appropriate
while(i < len(num)):
    for x in num:
        num[i] = str(x)
        if(len(str(x)) == 7):
            x = str(x)
            num[i] = x[0:1]+","+x[1:4]+","+x[4:7]
            i+=1
            continue
        if(len(str(x)) == 6):
            x = str(x)
            num[i] = x[0:3]+","+x[3:6]
            #print(num[i])
            i+=1
            continue
        if(len(str(x)) == 5):
            x = str(x)
            num[i] = x[0:2]+","+x[2:5]
            #print(num[i])
            i+=1
            continue
        if(len(str(x)) == 4):
            x = str(x)
            num[i] = x[0:1]+","+x[1:4]
            #print(num[i])
            i+=1
            continue
        else:
            x = str(x)
            num[i] = x
            #print(num[i])
            i+=1
            continue
        
end_time = time.time()
time = end_time - start_time

print("\nTotal time elapsed: " +format(time,"0.2f")+" seconds")

print("Red:       " + '{:>10}'.format(num[0]) + " ("+format((redRect/throws)*100,"0.2f")+"%)")
print("Blue:      " + '{:>10}'.format(num[1]) + " ("+format((blueCirc/throws)*100,"0.2f")+"%)")
print("Green:     " + '{:>10}'.format(num[2]) + " ("+format((greenRect/throws)*100,"0.2f")+"%)")
print("Dark Grey: " + '{:>10}'.format(num[3]) + " ("+format((dgreyCirc/throws)*100,"0.2f")+"%)")
print("Light Grey:" + '{:>10}'.format(num[4]) + " ("+format((lgreyCirc/throws)*100,"0.2f")+"%)")
print("Misses:    " + '{:>10}'.format(num[5]) + " ("+format((miss/throws)*100,"0.2f")+"%)")

