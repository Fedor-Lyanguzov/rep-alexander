"""
Ввести x, y целые.
Вывести все четные числа между x и y.
"""

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
