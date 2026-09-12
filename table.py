# table1.1
# for i in range(18,181,18):
#     print(i)


# table 1.2

# for i in range(1,11):
#     print(i*15)


# table 2.0


# start=eval(input("enter your 1st number of your0 table:-"))
# end=10*start+1
# for i in range(start,end,start):
#     print(i)


# table 2.1    

# start=eval(input("enter your 1st number of your0 table:-"))
# for i in range(1,11):
#     print(i*start)


# table 3.0    table+continue

start=eval(input("enter your 1st number of your0 table:-"))
end=10*start+1
for i in range(start,end,start):
    if i==48:
        continue
    print(i)


# table 3.1   perfect table

# start=eval(input("enter your 1st number of your0 table:-"))
# for i in range(1,11):
#     print(start,"*",i,"=",i*start)