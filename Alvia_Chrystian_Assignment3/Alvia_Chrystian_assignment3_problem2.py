a = input("Enter the first string: ")
b = input("Enter the second string: ")
c = input("Etner the third string: ")

#A < B
#A < C
#B < C
if((a.lower() < b.lower()) and (a.lower() < c.lower()) and (b.lower() < c.lower())):
    print("\n",a,"\n",b,"\n",c)
#----------------------------------------------------------------------------------------      
#A < B
#A < C
#B > C
elif((a.lower() < b.lower()) and (a.lower() < c.lower()) and (b.lower() > c.lower())):
    print("\n",a,"\n",c,"\n",b)
#----------------------------------------------------------------------------------------   
#A > B
#A < C
#B < C
elif((a.lower() > b.lower()) and (a.lower() < c.lower()) and (b.lower() < c.lower())):
    print("\n",b,"\n",a,"\n",c)
#----------------------------------------------------------------------------------------
#A > B
#A > C
#B < C
elif((a.lower() > b.lower()) and (a.lower() > c.lower()) and (b.lower() < c.lower())):
    print("\n",b,"\n",c,"\n",a)
#----------------------------------------------------------------------------------------
#A < B
#A > C
#B > C
elif((a.lower() < b.lower()) and (a.lower() > c.lower()) and (b.lower() > c.lower())):
    print("\n",c,"\n",a,"\n",b)
#----------------------------------------------------------------------------------------
#A > B
#A > C
#B > C
elif((a.lower() > b.lower()) and (a.lower() > c.lower()) and (b.lower() > c.lower())):
    print("\n",c,"\n",b,"\n",a)
