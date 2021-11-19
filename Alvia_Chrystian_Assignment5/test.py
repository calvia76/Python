import math
a = 31%11
x = 31%7
y = 31%5
z = 31%3
m = 31%2

#print(str(a)+"\n"+str(x)+"\n"+str(y)+"\n"+str(z)+"\n"+str(m))


def is_integer(n):
    n = (math.sqrt(n))
    if(isinstance(n, int)):
       return True
    else:
        return False

print(is_integer(144))
print(math.sqrt(144).is_integer())
