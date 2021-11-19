from My_Functions import *
import random

while(True):
    attempt = int(input("\nHow many problems would you like to attempt? "))
    if(attempt <= 0):
        print("INVALID ENTRY: Enter an integer greater than 0")
        continue
    else:
        break
    
while(True):
    width = int(input("\nHow wide do you want your digits to be? 5-10: "))
    if(10 < width or width < 5):
        print("INVALID ENTRY: Enter a number between 5 and 10")
        continue
    else:
        break
    
mode = False
while(True):
    mode_input = input("\nWould you like to activate 'drill' mode? yes or no: ")
    if(mode_input.lower() == "yes"):
        mode = True
        break
    if(mode_input.lower() == "no"):
        break
    
while(True):
    char = input("\nWhat character would you like to use? ")
    
    if(char.isnumeric()):
        print("INVALID ENTRY: Integer values not accepted, please enter a single character string")
    elif(len(char) > 1):
        print("String too long, try again")
        continue
    else:
        print("\nHere we go!")
        break


    
numbers = [1,2,3,4,5,6,7,8,9]
ops = ["+","-","/","%","*"]

total_add = 0
inc_add = 0

total_div = 0
inc_div = 0

total_sub = 0
inc_sub = 0

total_mod = 0
inc_mod = 0

total_mul = 0
inc_mul = 0

numCorrect = attempt
total = attempt
while(attempt!=0):
    print("\nWhat is ....")
    op = random.choice(ops)
    if(op == "+"):
        total_add+=1
    if(op == "/"):
        total_div+=1
    if(op == "-"):
        total_sub+=1
    if(op == "%"):
        total_mod+=1
    if(op == "*"):
        total_mul+=1
    num1 = random.choice(numbers)
    num2 = random.choice(numbers)
    if(op == "/"):
        while(True):
            test = eval(str(num1)+op+str(num2))
            if(test.is_integer()):
                break
            else:
                num1 = random.choice(numbers)
                num2 = random.choice(numbers)
                continue

    print_number(num1,width,char)
    print(operators(op,width,char))
    print_number(num2,width,char)
    if(mode):
        while(True):
            user_ans = int(input("= "))
            if(check_answer(num1, num2, user_ans, op)):
                print("Correct!\n")
                break
            else:
                if(op == "+"):
                    inc_add+=1
                if(op == "/"):
                    inc_div+=1
                if(op == "-"):
                    inc_sub+=1
                if(op == "%"):
                    inc_mod+=1
                if(op == "*"):
                    inc_mul+=1
                print("Incorrect! Try again.")
                continue
    else:
        user_ans = int(input("= "))
        if(check_answer(num1, num2, user_ans, op)):
            print("Correct!\n")
        else:
            numCorrect-=1
            if(op == "+"):
                inc_add+=1
            if(op == "/"):
                inc_div+=1
            if(op == "-"):
                inc_sub+=1
            if(op == "%"):
                inc_mod+=1
            if(op == "*"):
                inc_mul+=1
            print("Incorrect!\n")
    attempt-=1
    
#IF DRILL MODE IS NOT ACTIVE
if(not mode):
    print("\nYou got ",numCorrect, " out of ",total, " correct!")
    if(total_add == 0):
        print("\nNo addition problems presented")
    else:
        print("\nTotal addition problems presented: ",total_add)
        print("Correct addition problems: ", (total_add - inc_add),
              "(",float((total_add - inc_add)/total_add)*100,"%)")

    if(total_mul == 0):
        print("\nNo multiplication problems presented")
    else:
        print("\nTotal multiplication problems presented: ",total_mul)
        print("Correct multiplication problems: ", (total_mul - inc_mul),
              "(",float((total_mul - inc_mul)/total_mul)*100,"%)")

    if(total_sub == 0):
        print("\nNo subtraction problems presented")
    else:
        print("\nTotal subtraction problems presented: ",total_sub)
        print("Correct subtraction problems: ", (total_sub - inc_sub),
              "(",float((total_sub - inc_sub)/total_sub)*100,"%)")

    if(total_div == 0):
        print("\nNo division problems presented")
    else:
        print("\nTotal division problems presented: ",total_div)
        print("Correct division problems: ", (total_div - inc_div),
              "(",float((total_div - inc_div)/total_div)*100,"%)")
        
    if(total_mod == 0):
        print("\nNo modulus problems presented")
    else:
        print("\nTotal modulus problems presented: ",total_mod)
        print("Correct addition problems: ", (total_mod - inc_mod),
              "(",float((total_mod - inc_mod)/total_mod)*100,"%)")

#IF DRILL MODE IS ACTIVE
else:
    perfect = ""
    if(total_add == 0):
        print("\nNo addition problems presented")
    else:
        print("\nTotal addition problems presented: ",total_add)
        if(inc_add == 0):
            perfect = " (perfect!)"
        print("# of extra attempts needed: ", (inc_add),perfect)
        perfect = ""
        
    if(total_mul == 0):
        print("\nNo multiplication problems presented")
    else:
        print("\nTotal multiplication problems presented: ",total_mul)
        if(inc_mul == 0):
            perfect = " (perfect!)"
        print("# of extra attempts needed: ", (inc_mul),perfect)
        perfect = ""
        
    if(total_sub == 0):
        print("\nNo subtraction problems presented")
    else:
        print("\nTotal subtraction problems presented: ",total_sub)
        if(inc_sub == 0):
            perfect = " (perfect!)"
        print("# of extra attempts needed: ", (inc_sub),perfect)
        perfect = ""
        
    if(total_div == 0):
        print("\nNo division problems presented")
    else:
        print("\nTotal division problems presented: ",total_div)
        if(inc_div == 0):
            perfect = " (perfect!)"
        print("# of extra attempts needed: ", (inc_div),perfect)
        perfect = ""
        
    if(total_mod == 0):
        print("\nNo modulus problems presented")
    else:
        print("\nTotal modulus problems presented: ",total_mod)
        if(inc_mod == 0):
            perfect = " (perfect!)"
        print("# of extra attempts needed: ", (inc_mod),perfect)
        perfect = ""
print("\nThanks for playing!")









