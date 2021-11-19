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
    
def Sieve_Of_Eratosthenes(n):
    m = 2
    while (m*m <= n):
        if (sieve[m] == "P"):
            for i in range(m*m, n+1, m):
                sieve[i] = "N"
        m += 1

Sieve_Of_Eratosthenes(n)
sieve[0] = "N"
sieve[1] = "N"

i = 0
j = 0
while i != (n+1):
    if(sieve[i]=="P"):
        print('{:>3}'.format(str(i)), end =" ")
        j+=1
        i+=1
        if(j==10):
            j=0
            print("")
            continue
    else:
        i+=1
        continue
    


