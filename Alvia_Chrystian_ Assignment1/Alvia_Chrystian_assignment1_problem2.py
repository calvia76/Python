#Chrystian Alvia    2.10.21    202:01   Using the print function

#input variables for accepting keyboard inputs during runtime
name1 = input("Please enter name 1: ")
name2 = input("Please enter name 2: ")
name3 = input("Please enter name 3: ")

print("\n")

print("Here are your names in every possible order:")
print("--------------------------------------------")

#Empty print statements using '\n' for spaces between outputs
print("\n")

#print statements using the strings taken from keyboard input, concatenated by
#commas for punctuation correctness
print(name1 + ", " + name2 + ", " + name3)
print("\n")
print(name1 + ", " + name3 + ", " + name2)
print("\n")
print(name2 + ", " + name1 + ", " + name3)
print("\n")

#print statements using the strings taken from keyboard unput, concatenated by
#new line function '\n' to print names as a list
print(name2+"\n"+name3+"\n"+name1)
print("\n")
print(name3+"\n"+name2+"\n"+name1)
print("\n")
print(name3+"\n"+name1+"\n"+name2)
