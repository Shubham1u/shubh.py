user_list=[1,2,3,4,5]
if(list_length:=len(user_list))>3:
    print(f"The list is to long:-{list_length} elements")


# ex 2.1.........................

while(command:=input("Enter command:-"))!="quit":
    print(f"executing:-{command}.......")