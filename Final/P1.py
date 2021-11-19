
#A
def stringify_digit(num):
    value = f'{num}'
    return value


#B
def reverse(string):
    i=len(string)
    temp = ""
    while(i!=0):
        temp+=string[i-1]
        i-=1
    return temp


print(reverse("test"))

#C
def stringify(num):
    return stringify_digit(num)


if(stringify(-123) == "-123"):
    print("TRUE")
else:
    print("FALSE")


