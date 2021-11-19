while(True):
    budget = float(input("Enter the budget for your pizza party "))
    if(budget < 0):
        print("Invalid entry, Try again!")
        continue
    elif(budget == 0):
        print("You'll need money to have a pizza party!")
        exit()
    else:
        break
while(True):
    cps = float(input("Cost per slice of pizza: "))
    if(cps < 1):
        print("Invalid entry, try again!")
        continue
    else:
        break
while(True):
    cpwp = float(input("Cost per whole pizza: "))
    if(cpwp < 1):
        print("Invalid entry, try again!")
        continue
    else:
        break
while(True):
    ppl = float(input("How many people will be attending your party? "))
    if(ppl < 1):
        print("Invalid entry, try again!")
        continue
    else:
        break
p = 1
bizza = []
while(p <= ppl):
    eat = int(input("Enter number of slices for person #" + str(p) + ": "))
    if(eat <= 0 ):
        print("Invalid entry, try again!")
        continue
    else:
        bizza.append(eat)
        p+=1
        continue
pies = 0
extra = 0
slices = 0
for x in bizza:
    slices += x
    if(slices >= 8):
        slices = slices - 8
        extra += slices
        if(slices >= 8):
            pies += 1
            slices = 0
        counter = 0
        pies += 1
        continue
#print("Pies: " + str(pie) + "\nSlices: " + str(slices))
    
cps = cps * slices
cpwp = cpwp * pies
total = cps+cpwp

if(budget < total):
    over = (budget - total)*-1
    print("\nYour order cannont be completed")
    print("You would need to purchase " + str(pies) + " pies and " + str(slices) + " slices.")
    print("This would put you over budget by $" + str(over))
else:
    remain = budget - total
    print("\nYou should purchase " + str(pies) + " pie(s) and " + str(slices) + " slice(s)")
    print("Your total cost will be $" +str(total))
    if(remain == 0):
        print("You will have no money left after your order.")
    else:
        print("Your will still have $" + str(remain) + " after your order")















    
