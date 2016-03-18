"""
Для любых a, b, введенных с клавиатуры, решить уравнение
 a*x + b = 0
"""

a = float(input())
b = float(input())
if a!=0:
    x = -b/a
    print (x)
elif b==0:
    print("x - any number")
else :
    print ("x - no numbers")
