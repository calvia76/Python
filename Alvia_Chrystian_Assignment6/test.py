import math

while True:
    n = int(input("Enter highest integer value, n, to evaluate prime numbers between 0 - n: "))
    if(n<0):
        print("Invalid Entry: Enter a positive integer")
        continue
    if(0 < n < 10):
        print("Invalid Entry: Enter an integer greater than 10")
    else:
        break

sieve = []
for x in range(0,n+1):
    sieve.append("P")

sieve[0]= "N"
sieve[1] = "N"

correction = 0
def prime_check(array, divisor):
    counter = 0
    correction = divisor+1
    dividend = divisor+1
    
    while counter != (n-correction)+1:
        if(dividend % divisor == 0):
            sieve[dividend] = "N"
            dividend += 1
            counter+=1
        else:
            dividend +=1
            counter+=1
            continue
        
def sqrt_check(array):
    i = 121
    while(i != n+1):
        if(math.sqrt(i).is_integer()):
            sieve[i] = "N"
            i+=1
        else:
            i+=1
            continue
            
        
if(n >=121):
    prime_check(sieve,2)
    prime_check(sieve,3)
    prime_check(sieve,4)
    prime_check(sieve,5)
    prime_check(sieve,6)
    prime_check(sieve,7)
    prime_check(sieve,11)
    prime_check(sieve,13)
    prime_check(sieve,19)

    sqrt_check(sieve)
    
elif(n >= 42):
    prime_check(sieve,2)
    prime_check(sieve,3)
    prime_check(sieve,4)
    prime_check(sieve,5)
    prime_check(sieve,6)
    prime_check(sieve,7)
    
elif(n >= 25):
    prime_check(sieve,2)
    prime_check(sieve,3)
    prime_check(sieve,5)
    
elif(n < 25):
    prime_check(sieve,2)
    prime_check(sieve,3)
    
primes = []
i = 0
while i != (n+1):
    if(sieve[i]=="P"):
        primes.append(i)
        i+=1
    else:
        i+=1
        continue
    
j = 0
n = 0
for x in primes:
    j+=1
    print('{:>3}'.format(primes[n]), end =" ")
    n+=1
    if(j==10):
        j=0
        print("")
        continue
