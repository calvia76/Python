while(True):
    x = int(input("Enter a non-negative integer: "))
    if(x < 0):
        print("Sorry that is not valid!")
        continue
    else:
        cont = input("Do you wish to continue? ")
        if(cont.lower() == "no"):
            print("Finished!")
            exit()
        elif(cont.lower() == "yes"):
            count = 0
            n1 = 0
            n2 = 1
            n = 0
            total= []
            while count <= x:
                total.append(n1)
                n = n1 + n2
                n1 = n2
                n2 = n
                count+=1
                
            for j in range(len(total)):
                print(total[j],end=",")
            print()
