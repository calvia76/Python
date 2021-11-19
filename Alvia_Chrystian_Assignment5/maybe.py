start = int(input("Starting number: "))
end = int(input("Ending number: "))


count = 0
max_len = len(str(end))
for i in range(start, end+1):
    divisor = 0
    for x in range(1,i+1):
        if(i % x == 0):
            divisor+=1
    if(divisor == 2):
        digits = len(str(i))
        spaces = max_len - digits
        print((" " * spaces) + str(i), end=" ")
        count+=1
        if(count == 10):
            count = 0
            print()









