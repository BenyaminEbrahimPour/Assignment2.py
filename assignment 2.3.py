print("Enter first name::  ")
print("Enter last name::  ")
x1 = float(input("Enter score of structural analysis::  "))
x11 = float(input("Enter weight of structural analysis::  "))
x2 = float(input("Enter score of fluid mechanics::  "))
x22 = float(input("Enter weight of fluid mechanics::  "))
x3 = float(input("Enter score of soil mechanics:: "))
x33= float(input("Enter weight of soil mechanics:: "))
sum = x11 + x22 + x33
average = ((x1*x11)+(x2*x22)+(x3*x33))/sum
if average >= 17 :
    print("Great")
if  12 <= average < 17 :
    print("Normal")
if average < 12 :
    print("Fail")
