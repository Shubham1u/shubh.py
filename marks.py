Hindi=int(input("Enter marks in Hindi: "))
English=int(input("Enter marks in English: "))
Maths=int(input("Enter marks in Maths: "))
Science=int(input("Enter marks in Science: "))
Sst=int(input("Enter marks in Social Science: "))
total_marks=Hindi+English+Maths+Science+Sst
print("Total marks obtained:", total_marks)
average_marks=total_marks/5
print("Average marks:", average_marks)
if 90>=80:
    print("excellent")
elif  80>=70:
    print("good")
elif  70>=60:
    print("first")
elif 60>=50:
    print("second")
elif 50>=40:
    print("third")
elif  40>=35:
    print("pass")
else:
    print("fail")