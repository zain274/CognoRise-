num1=int(input("Enter the value:"))
num2=int(input("Enter the value:"))
opr=input("Enter opr...(+,-,*,/)")
if opr=="+":
    print(num1+num2)
if opr=="-":
    print(num1-num2)
if opr=="*":
    print(num1*num2)
if opr=="/":
    print(num1/num2)
    
if opr!="+" and opr!="-" and opr!="*" and opr!="/":
    print("Invalid opr:")
