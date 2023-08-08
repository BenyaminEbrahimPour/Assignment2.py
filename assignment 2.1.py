from cmath import cos, sin, sqrt, tan
pi = 3.14
print('sin---> 1')
print('cos---> 2')
print('tan---> 3')
print('cot---> 4')
print('factorial---> 5')
print('radical---> 6')
x = int(input("enter the number from list:"))
if x==1 :
    d=float(input(":"))
    s=sin((d*pi)/180)
    print(s)
if  x==2 :
    d=float(input(':')) 
    s=cos((d*pi)/180)
    print(s)  
if x==3 :
    d=float(input(":"))
    s=tan((d*pi)/180)
    print(s)  
if x==4 :
    d=float(input(":"))
    s=tan((d*pi)/180)
    print(1/s)      
if x==5 :
    d=int(input(":"))
    from math import factorial
    s=factorial(d)
    print(s)

if x==6 :
    d=float(input(":"))
    print(sqrt(d))






