a=int(input("enter a first number: "))
operator=input("enter an operator (+, -, *, /): ")
b=int(input("enter a second number: "))
operators=input("enter an operator (+, -, *, /): ")
c=int(input("enter a third number: "))
if operator=='+':
    print("result:",a+b+c)
elif operator=='-':
    print("result:",a-b-C)
elif operator=='*':
    print("result:",a*b*C)
elif operator=='/':
    print("result:",a/b/C)
else:   
        print("Error: Division by zero is not allowed.")