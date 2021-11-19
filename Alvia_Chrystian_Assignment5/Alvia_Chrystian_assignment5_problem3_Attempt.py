import math
start = int(input("Starting number: "))
end = int(input("Ending number: "))

i = start
prime = []
if(i == 1):
   i+=1
   prime.append(i)
   
elif(i == 2):
    prime.append(i)
    i+=1

    
while(i<end+1):
    
    if(i%2 == 0):
        i+=1
        continue
    elif((i%3 == 0) or (i%5==0) or (i%7==0))and i > 8:
        i+=1
        continue
    elif((i%11==0) and i > 11):
        i+=1
        continue
    
    elif(math.sqrt(i).is_integer()):
        i+=1
        continue
    else:
        prime.append(i)
        i+=1
        continue
j = 0
n = 0
for x in prime:
    j+=1
    print('{:>3}'.format(prime[n]), end =" ")
    n+=1
    if(j==10):
        j=0
        print("")
        continue
    
        

        
