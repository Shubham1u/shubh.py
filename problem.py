# # QUESTION 1

# user_name = str(input("enter your name :"))
# district = str(input("enter your district name :"))
# age = int(input("enter your age :"))

# if district == "jaipur":
#     if age >= 16:
#         print("you are eligible for driving licence")
#     else:
#         print("you are not eligible for driving licence")
# else:
#     if age >= 18:
#         print("you are eligible for driving licence")
#     else:
#         print("you are not eligible for driving licence")

# print("------------------------------------------------------------------------------")

# #QUESTION 2

# s = int(input("enter number : "))
# for i in range(1, s + 1):
#     print(" " * (s - i) + "* " * i) 

# print("--------------------------------------------------------------------------------")

# # QUESTION 3

n = int(input("enter  numbers :"))
a = 0
b = 1
for i in range (n):
    print(a)
    c=a+b
    a=b
    b=c
# print("----------------------------------------------------------------------------------")
    
# # QUESTION 4 

# s = input("enter a string: ")
# if s == s[: :-1]:
#     print("pelindrome")
    
# else:
#     print("not pelindrome")
    

# # print("QUESTION 5..................................................")


# prime = int(input("enter a number to check if it's prime : "))
# if prime<=1:
#     print(prime,"is not a prime number")
# elif prime > 1:
#     for i in range(2, int(prime//2)+1):
#         if (prime % i) == 0:
#             print(prime, "is not a prime number")
#             break
#     else:
#         print(prime, "is a prime number")