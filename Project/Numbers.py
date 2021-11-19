print("Main Menu\n")
print("1 - Find all prime numbers within a given range\n")
print("2 - Find all perfect numbers within a given range\n")
print("3 - Find all abundant numbers within a given range\n")
print("4 - Chart all even, odd, prime, perfect, and abundant numbers within a given range\n")
print("5 - Quit\n\n\n")

while(True):
    try:
        choice = int(input("Your choice: "))
        if(choice > 5 or choice < 1):
            print("INVALID ENTRY: Enter a number between 1-5")
        else:
            break
    except:
        print("I don't understand...")
        continue

if(choice == 5):
    quit()

    
while(True):
    try:
        start = int(input("Enter starting number (positive only): "))
        if(start < 0):
            print("INVALID ENTRY: Enter a positive integer")
            continue
        else:
            while(True):
                try:
                    end = int(input("Enter ending number (positive only): "))
                    if(end < 0):
                        print("INVALID ENTRY: Enter a positive integer")
                        continue
                    if(start >= end):
                        print("INVALID ENTRY: Enter an integer greater than starting value")
                        continue
                    else:
                        break
                except:
                    print("I don't understand...")
                    continue
            break
    except:
        print("I don't understand...")
        continue
print()

    
def is_even(num):
    if(num%2==0):
        return True
    else:
        return False

def is_odd(num):
    if(num%2!=0):
        return True
    else:
        return False
########################################################
############### PRIME FUNCTIONS ########################
########################################################
def all_prime(start,end):
    if(start == 0):
        start+=2
    if(start == 1):
        start+=1
    for x in range(start,end):
        if(is_prime(x)):
            print(x)
        else:
            continue
def is_prime(num):
    flag = False
    if(num == 0):
        return False
    if(num == 1):
        return False
    if(num > 1):
        for i in range(2,num):
            if(num%i == 0):
                flag = True
                break
    if(flag):
        return False
    else:
        return True
########################################################
############### PERFECT FUNCTIONS ######################    
########################################################
def all_perfect(start,end):
    if(start == 0):
        start+=1
    for x in range(start,end):
        if(is_perfect(x)):
            print(x)
        else:
            continue
def is_perfect(num):
    if(num == 0):
        return False
    factors = []
    total = 0
    for i in range(1,num):
        if(num%i==0):
            factors.append(i)
    for x in factors:
        total += x
    if(total == num):
        return True
    else:
        return False
########################################################
############## ABUNDANT FUNCTIONS ######################    
########################################################
def all_abundant(start,end):
    for x in range(start,end+1):
        if(is_abundant(x)):
            print(x)
        else:
            continue

def is_abundant(num):
    factors = []
    total = 0
    for i in range(1,num):
        if(num%i==0):
            factors.append(i)
    for x in factors:
        total+=x
    if(total > num):
        return True
    else:
        return False
########################################################
############### CHART FUNCTIONS ########################
########################################################
def chart(start,end):
    counter = 0
    x = "x"
    
    for i in range(start,end+1):
        even = ""
        odd = ""
        prime = ""
        perf = ""
        abun = ""
        if(is_even(i)):
            even += x
        if(is_odd(i)):
            odd += x
        if(is_prime(i)):
            prime += x
        if(is_perfect(i)):
            perf += x
        if(is_abundant(i)):
            abun += x
        print("%-10s"%i+"%-10s"%even+"%-10s"%odd+"%-10s"%prime+"%-10s"%perf+"%-10s"%abun)
        


########################################################
if(choice == 1):
    print("All prime numbers between ", start," and ",end)
    print("#############")
    all_prime(start,end)
    print("#############")
    
if(choice == 2):
    print("All perfect numbers between ", start," and ",end)
    print("#############")
    all_perfect(start,end)
    print("#############")
    
if(choice == 3):
    print("All abundant numbers between ", start," and ",end)
    print("#############")
    all_abundant(start,end)
    print("#############")
    
if(choice == 4):
    print("%-10s"%"Number"+"%-10s"%"Even"+"%-10s"%"Odd"+"%-10s"%"Prime"+"%-10s"%"Perfect"+"%-10s"%"Abundant")
    chart(start,end)
    print()

    


                
