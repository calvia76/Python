#UNIVERSAL LISTS
empty = []

#A ******************************************************************

def listlen(array):
    i=0
    for x in array:
        i+=1
    return i
    
#TEST CASES
lentest = [1,2,3]
lentest2 = ["A",123,"B","APPLESAUCE",394,312]
lentest3 = [1284,1274,1212,1201,1284,1237,1732,1034,847,4856,1484,1943,3283]

print("LIST LENGTH TEST 1: ",listlen(lentest),lentest)
print("LIST LENGTH TEST 2: ",listlen(lentest2),lentest2)
print("LIST LENGTH TEST 3: ",listlen(lentest3),lentest3)
print("LIST LENGTH TEST 4: ",listlen(empty))

#B ******************************************************************

def listmax(array):
    if(listlen(array) == 0):
        return None
    i=0
    n = 1
    temp = 0
    count = 0
    while(count!= listlen(array)-1):
        if(array[i] > array[n]):
            temp = array[i]
            n+=1
            count+=1
        elif(array[i] < array[n]):
            temp = array[n]
            i=n
            n+=1
            count+=1
        else:
            n+=1
            count+=1
    return temp

#TEST CASES
maxtest = [69,54,42,4,73,9,5,22,420,720]
maxtest2 = [1284,1274,1212,1201,1284,1237,1732,1034,847,4856,1484,1943,3283]

print("\nMAX TEST 1: ",listmax(maxtest),maxtest)
print("MAX TEST 2: ",listmax(maxtest2),maxtest2)
print("MAX TEST 3: ",listmax(empty))

#C ******************************************************************

def listcopy(array):
    if(listlen(array) == 0):
        x = []
        return x
    x = []
    x = array
    return x

#TEST CASES
copytest = [1,2,3]
copytest2 = ["A",123,"B","APPLESAUCE",394,312]

print("\nCOPYLIST TEST 1: ",listcopy(copytest))
print("COPYLIST TEST 2: ",listcopy(copytest2))
print("COPYLIST TEST 3: ",listcopy(empty))

#D ******************************************************************

def listappend(array, value):
    temp = [value]
    array = array + temp
    return array

#TEST CASES
appendtest = [1,2,3]

print("\nAPPEND TEST 1: ",listappend(appendtest,4))
print("APPEND TEST 2: ",listappend(appendtest,"test"))

#E ******************************************************************

def listinsert(array, index, value):
    value = [value]
    half1 = []
    half2 = []
    newArray = []
    temp = 0
    i=0
    #For insertion at end of list
    if(index == listlen(array)):
        while(i!=listlen(array)):
            temp = array[i]
            half2 = half2 + [temp]
            i+=1
        newArray = half2+value
        return newArray
    #For insertion anywhere else
    else:
        while(i!=index):
            temp = array[i]
            half1 = half1 + [temp]
            i+=1
        while(i!=listlen(array)):
            temp = array[i]
            half2 = half2 + [temp]
            i+=1
        newArray = half1 + value + half2
        return newArray

#TEST CASES
inserttest = [1,2,3,5,6] #Middle of list
inserttest2 = [1,2,3,4,5] #End of list
inserttest3 = [2,3,4,5,6] #Front of list
inserttest4 = [1,3,4,5,6]

print("\nINSERTION TEST 1: ",listinsert(inserttest,3,4))
print("INSERTION TEST 2: ",listinsert(inserttest2,5,6))
print("INSERTION TEST 3: ",listinsert(inserttest3,0,1))
print("INSERTION TEST 4: ",listinsert(inserttest4,1,"test"))

#F ******************************************************************

def listremove(array, value):
    temp = 0
    i=0
    newArray = []
    while(i!=listlen(array)):
            temp = array[i]
            if(temp == value):
                i+=1
                continue
            else:
                newArray = newArray + [temp]
                i+=1
    return newArray

#TEST CASES
removetest = [1,2,3,4,5,6] #Middle of list
removetest2 = [1,2,3,4,5,6] #End of list
removetest3 = [1,2,3,4,5,6] #Front of list
removetest4 = [1,3,"test",4,5,6] #String removal
removetest5 = [1,2,3,4,3,5,3,7,3,9,10,3] #Multiple items

print("\nREMOVE TEST 1: ",listremove(removetest,4))
print("REMOVE TEST 2: ",listremove(removetest2,6))
print("REMOVE TEST 3: ",listremove(removetest3,1))
print("REMOVE TEST 4: ",listremove(removetest4,"test"))
print("REMOVE TEST 5: ",listremove(removetest5,3))

#G ******************************************************************

def listreverse(array):
    temp = 0
    i = listlen(array)-1
    newArray = []
    while(i!=-1):
            temp = array[i]
            newArray = newArray + [temp]
            i-=1
    return newArray

#TEST CASES
reversetest = [1,2,3,4,5,6]
reversetest2 = ['A','B','C','D']

print("\nREVERSE TEST 1: ",listreverse(reversetest))
print("REVERSE TEST 2: ",listreverse(reversetest2))















    
