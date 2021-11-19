


histogram = input("Enter a series of numbers separated by spaces: ")

temp = ""
tempList = []
for x in histogram:
    if(x == " "):
        tempList.append(temp)
        temp = ""
        continue
    temp+=x
tempList.append(temp)
histList = []
for x in tempList:
    if(x.isnumeric()):
        if(int(x) < 0 or int(x) > 10):
            print(x, " is out of bounds - rejecting")
            continue
        else:
            print(x, " is valid - accepting")
            histList.append(x)
            continue
            
    else:
        print(x + " is not a number")
        continue


print("Largest Number:" ,max(histList))
print("Smallest Number:" ,min(histList))
print("Range of values:" , int(max(histList))-int(min(histList)))
print("Mode:" , max(set(histList),key=histList.count))
print("Frequency of histogram:")
