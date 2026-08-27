a=int(input("enter first number:"))
b=int(input("enter second number:"))
opr=input("enter operator: (+,-,*,/,%)")
if opr=="+":
    print("addition is", a+b)
elif opr=="-":
    print("subtraction is", a-b)
elif opr=="*":
    print("multiplication is", a*b)
elif opr=="/":
    print("division is", a/b)
elif opr=="%":
    print("modulus is", a%b)
else:
    print("invalid operator")