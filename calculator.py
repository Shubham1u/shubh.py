a=eval(input("enter a first number: "))
operator=input("enter an operator (+, -, *, /): ")
b=eval(input("enter a second number: "))
operators=input("enter an operator (+, -, *, /): ")
c=eval(input("enter a third number: "))
if operator=='+':
    print("result:",a+b+c)
elif operator=='-':
    print("result:",a-b-c)
elif operator=='*':
    print("result:",a*b*c)
elif operator=='/':
    print("result:",a/b/c)
else:   
        print("Error: Division by zero is not allowed.")
