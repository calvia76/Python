import math

def horizontal_line(width, char):
    temp = ""
    while(width!=0):
        width-=1
        temp+=char
    return temp
    

def vertical_line(shift, height, char):
    temp = ""
    while(height!=0):
        if(shift!=0):
            for x in range(0,shift):
                temp += " "
        if(height==1):
            temp += char
            return temp
        else:
            temp += char+"\n"
            height-=1
    return temp
        
            
def two_vertical_lines(width, height, char):
    temp = ""
    while(height!=0):
        temp += char
        if(width == 0):
            if(height==1):
                temp += char
                return temp
            temp += char+"\n"
            height-=1
            continue
        elif(width!=0):
            for x in range(0, width-2):
                temp += " "
            if(height==1):
                temp += char
                return temp
            temp += char+"\n"
            height-=1
    return temp

#---------------------------------------------------------------

def number_zero(width,char):
    row1 = horizontal_line(width,char)
    row2 = two_vertical_lines(width, 3 ,char)
    row3 = horizontal_line(width,char)
    num = row1 +"\n" + row2 +"\n"+ row3  + "\n"
    return num
    
def number_one(width, char):
    num = vertical_line(width-1,5,char)
    return num + "\n"

def number_two(width, char):
    row1 = horizontal_line(width, char)
    row2 = vertical_line(width-1,1,char)
    row3 = horizontal_line(width, char)
    row4 = vertical_line(0,1,char)
    row5 = horizontal_line(width, char)
    num = row1 +"\n" + row2 +"\n"+ row3 + "\n" + row4 + "\n" +row5 + "\n"
    return num

def number_three(width, char):
    row1 = horizontal_line(width, char)
    row2 = vertical_line(width-1,1,char)
    row3 = horizontal_line(width, char)
    row4 = vertical_line(width-1,1,char)
    row5 = horizontal_line(width, char)
    num = row1 +"\n" + row2 +"\n"+ row3 + "\n" + row4 + "\n" +row5 + "\n"
    return num

def number_four(width, char):
    row1 = two_vertical_lines(width,2,char)
    row2 = horizontal_line(width,char)
    row3 = vertical_line(width-1,2,char)
    num = row1 +"\n" + row2 +"\n"+ row3 + "\n"
    return num 

def number_five(width, char):
    row1 = horizontal_line(width, char)
    row2 = vertical_line(0,1,char)
    row3 = horizontal_line(width, char)
    row4 = vertical_line(width-1,1,char)
    row5 = horizontal_line(width, char)
    num = row1 +"\n" + row2 +"\n"+ row3 + "\n" + row4 + "\n" +row5 + "\n"
    return num

def number_six(width, char):
    row1 = horizontal_line(width, char)
    row2 = vertical_line(0,1,char)
    row3 = horizontal_line(width, char)
    row4 = two_vertical_lines(width, 1, char)
    row5 = horizontal_line(width, char)
    num = row1 +"\n" + row2 +"\n"+ row3 + "\n" + row4 + "\n" +row5 + "\n"
    return num

def number_seven(width, char):
    row1 = horizontal_line(width, char)
    row2 = vertical_line(width-1,4,char)
    num = row1 +"\n" + row2 +"\n"
    return num

def number_eight(width, char):
    row1 = horizontal_line(width, char)
    row2 = two_vertical_lines(width, 1, char)
    row3 = horizontal_line(width, char)
    row4 = two_vertical_lines(width, 1, char)
    row5 = horizontal_line(width, char)
    num = row1 +"\n" + row2 +"\n"+ row3 + "\n" + row4 + "\n" +row5 + "\n"
    return num

def number_nine(width,char):
    row1 = horizontal_line(width, char)
    row2 = two_vertical_lines(width, 1, char)
    row3 = horizontal_line(width, char)
    row4 = vertical_line(width-1,2,char)
    num = row1 +"\n" + row2 +"\n"+ row3 + "\n" + row4 + "\n"
    return num

def print_number(num, width, char):
    if(num == 0):
        print(number_zero(width,char))
    if(num == 1):
        print(number_one(width,char))
    if(num == 2):
        print(number_two(width,char))
    if(num == 3):
        print(number_three(width,char))
    if(num == 4):
        print(number_four(width,char))
    if(num == 5):
        print(number_five(width,char))
    if(num == 6):
        print(number_six(width,char))
    if(num == 7):
        print(number_seven(width,char))
    if(num == 8):
        print(number_eight(width,char))
    if(num == 9):
        print(number_nine(width,char))

def operators(op, width, char):
    shift = 0
    space = ""
    sign = ""
    if(op == "-"):
        sign = (horizontal_line(width,char))
        return sign + "\n"
    if(op == "*"):
        if(width%2==0):
            shift = (width/2)-1
        else:
            shift = ((width+1)/2)-1
        row1 = two_vertical_lines(width,1,char)
        row2 = vertical_line(int(shift),1,char)
        row3 = two_vertical_lines(width,1,char)
        sign = row1 + "\n" + row2 + "\n" + row3 + "\n"
        return sign
    if(op == "/"):
        temp = width
        while(temp>0):
            for m in range(1,temp):
                print(" ",end="")
            for n in range(0,1):
                print("*",end="")
            print()
            temp-=1
    if(op == "%"):
        temp = width
        while(temp>0):
            for m in range(1,temp):
                if(temp==width-1):
                    for x in range(1,temp-1):
                        print(" ",end="")
                    break
                print(" ",end="")
            for n in range(0,1):
                if(temp==width-1):
                    print("O",end="")
                print("*",end="")
                if(temp==2):
                    print("O",end="")
            print()
            temp-=1
    if(op == "+"):
        if(width%2==0):
            shift = (width/2)-1
            for x in range(0,int(shift)):
                space += " "
            row1 = space + two_vertical_lines(1,1,char) + "\n" + space + two_vertical_lines(1,1,char)
        else:
            shift = ((width+1)/2)-1
            row1 =  vertical_line(int(shift),1,char) + "\n" + vertical_line(int(shift),1,char)
        
        row2 = horizontal_line(width,char)
        sign = row1 + "\n" + row2 + "\n" + row1 + "\n"
    return sign



def check_answer(num1, num2, ans, operator):
    actual = eval(str(num1)+operator+str(num2))
    if(actual == ans):
        return True
    else:
        return False
  























