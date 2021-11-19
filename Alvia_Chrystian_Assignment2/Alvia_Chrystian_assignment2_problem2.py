v1 = int(input("\nEnter value 1: "))
v2 = int(input("Enter value 2: "))

# v1
ones1 = v1 % 10
v1 = v1-ones1
         
tens1 = v1% 100
v1 = v1 - tens1
ans10_1 = tens1/10

hunds1 = v1 % 1000
v1= v1 - hunds1
ans100_1 = hunds1/100

thous1 = v1 % 10000
v1 = v1 - thous1
ans1000_1 = thous1/1000

#v2
ones2 = v2 % 10
v2 = v2-ones2
         
tens2 = v2% 100
v2 = v2 - tens2
ans10_2 = tens2/10

hunds2 = v2 % 1000
v2= v2 - hunds2
ans100_2 = hunds2/100

thous2 = v2 % 10000
v2 = v2 - thous2
ans1000_2 = thous2/1000

print("\n\tPlace Value Totals:\n")

print("\t",ones1," + ", ones2, " = ", ones1+ones2, " one(s)")
print("\t",int(ans10_1)," + ", int(ans10_2), " = ", int(ans10_1+ans10_2), " ten(s)")
print("\t", int(ans100_1), " + ", int(ans100_2), " = ", int(ans100_1+ans100_2), " hundred(s)")
print("\t", int(ans1000_1), " + ", int(ans1000_2), " = ", int(ans1000_1+ans1000_2), " thousand(s)")

