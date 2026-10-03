# def print_fibonacci():
#     n = int(input("enter  numbers :"))
#     a = 0
#     b = 1
#     for i in range (n):
#         print(a)
#         c=a+b
#         a=b
#         b=c
 
# def calculate_factorial():
#     a = int(input("Enter number: "))
#     fact = 1

#     for m in range(a, 0, -1):
#         fact = fact * m
#     print("Factorial =", fact)

# def check_prime():
#     prime = int(input("enter a number to check if it's prime : "))
#     if prime<=1:
#         print(prime,"is not a prime number")
#     elif prime > 1:
#         for i in range(2, int(prime//2)+1):
#             if (prime % i) == 0:
#                 print(prime, "is not a prime number")
#                 break
#         else:
#             print(prime, "is a prime number")

# print("1.fibonacii")
# print("2.factorial")
# print("3.prime")
# X=int(input("enter your choice:-"))
# if X==1:
#     print_fibonacci()
# elif X==2:
#     calculate_factorial()
# elif X==3:
#     check_prime()
# else:
#     print("invalid")

