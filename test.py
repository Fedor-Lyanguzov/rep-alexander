print ("hw")
from math import *

x = int(input())
y = int(input())

if x>y :
    t = x
    x = y
    y = t
if x%2 ==0:
    x+=1
for i in range(x,y,2):
    print(i)
    
"""               
if x>y and x%2 !=0 and y%2 !=0 : 
    for i in range(x, y, -1):
        if i%2 !=0:
            print (i) 
else :
    print("incorrect input")
"""    
    
    
#    x = x+2






"""
print("Hello World!")
a = float(input())
b = float(input())
if a!=0:
    x = -b/a
    print (x)
elif b==0:
    print("x - any number")
else :
    print ("x - no numbers")
"""
"""x = int(input())

if x<100 and x>9:
    print ("true")
else : 
    print ("false")
"""



"""x = float (input())
print (abs(x), x*x, x*pi, atan(x), tan(x) )
"""

"""y = sin(pi) + cos(pi)
a = atan(1)
print(a/pi*180)
"""
"""
x = int(input())
print(x+1, x*2, abs(x), x*x)
"""