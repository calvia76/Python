#Chrystian Alvia    2.10.21    202:01   Math Expressions

#For this I used the exact conversion numbers for simplicity, rather than
#storing each conversion equation result for each measurement in a
#variable then printing the variable in a print statement. 

#input function accepting, presumably, numbers only for program to work.
mL = input("How many ml?")
print("\n")
print("--------------------------------------------------\n\tmL to US Fluid Volume Units\n--------------------------------------------------")
#taking input 'mL' and converting to type float, then multiplying by the conversion number and printing result
print("mL:\t\t" + str(float(mL)))
print("tsp:\t\t" + str(float(mL)*0.202884))
print("tbsp:\t\t" + str(float(mL)*0.067628))
print("cup(s):\t\t" + str(float(mL)*0.00422675))
print("pint(s):\t" + str(float(mL)*0.00211338))
print("quart(s):\t" + str(float(mL)*0.00105669))
print("gallon(s):\t" + str(float(mL)*0.000264172))
print("fl oz:\t\t" + str(float(mL)*0.033814))
print("--------------------------------------------------")

