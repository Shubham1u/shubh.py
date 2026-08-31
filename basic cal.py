a=eval(input("enter a first number: "))
operator=input("enter an operator (+, -, *, /): ")
b=eval(input("enter a second number: "))
if operator=='+':
    print("result:",a+b)
elif operator=='-':
    print("result:",a-b)
elif operator=='*':
    print("result:",a*b)
elif operator=='/':
    print("result:",a/b)
else:   
    print("Error: Division by zero is not allowed.")