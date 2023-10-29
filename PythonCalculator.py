def addition(fnum,snum):
    return fnum+snum

def subtraction(fnum,snum):
    return fnum-snum

def multiplication(fnum,snum):
    return fnum*snum

def division(fnum,snum):
    return fnum,snum

def mod(fnum,snum):
    return f'{fnum}%{snum}=' 
    fnum%snum

operand=input("please enter your operand (+,-,*,/,%)")

fnum=int(input("Please enter the first number"))
snum=int(input("Please enter the second number"))
#print(type(fnum))
#print(type(snum))

if operand=="+":
    print(addition(fnum,snum))

elif operand=="-":
    print(subtraction(fnum,snum))

elif operand=="%":
    print(mod(fnum,snum))

elif operand=="*":
    print(multiplication(fnum,snum))

elif operand=="/":
    print(division(fnum,snum))

else :
    print("Operand entered not found")


