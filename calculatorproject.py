def add(num1,num2):
    return(num1+num2)
def substract(num1,num2):
    return(num1-num2)
def multiply(num1,num2):
    return(num1*num2)
def divide(num1,num2):
    return(num1/num2)
def modulus(num1,num2):
    return(num1%num2)
import math
def sqrt(num):
    return(math.sqrt(num))
def exponential(num):
    return(math.exp(num))
def sine(num):
    return(math.sin(math.radians(num)))
def cos(num):
    return(math.cos(math.radians(num)))
def tan(num):
    return(math.tan(math.radians(num)))
def degrees(num):
    return(math.radians(num))
def radians(num):
    return(math.degrees(num))




while True:
    choice=input("enter your choice (1/2/3/4/5/6/7/8/9/10/11/12/ : ")
    if choice in ('1','2','3','4','5',):
        num1=float(input("enter first num:"))
        num2=float(input("enter second num:"))
        if choice == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif choice == '2':
            print(num1,'-',num2,'=',substract(num1,num2))
        elif choice == '3':
            print(num1,'*',num2,'=',multiply(num1,num2))
        elif choice =='4':
            print(num1,'/',num2,'=',divide(num1,num2))
        elif choice == '5':
            print(num1,'%',num2,'=',modulus (num1,num2))
        next_calculation = input("let do next calculation(yes/no):")
        if next_calculation == "no":
            break
        else:
            continue
    if choice in ('6','7','8','9','10','11','12',):
        num=float(input("enter value:"))
       
        
        if choice == '6':
            print(math.sqrt(num))
        elif choice == '7':
            print(math.exp(num))
        elif choice == '8':
            print(math.sin(math.radians(num)))
        elif choice == '9':
            print(math.cos(math.radians(num)))
        elif choice == '10':
            print(math.tan(math.radians(num)))
        elif choice == '11':
            print(math.radians(num))
        elif choice == '12':
            print(math.degrees(num))
        next_calculation = input("let do next calculation(yes/no):")
        if next_calculation == "no":
            break
    else:
        continue