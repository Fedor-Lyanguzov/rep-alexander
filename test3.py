print('hw')

def plus(a,b):
    c = a+b
    return (a+b)**c

#print(plus(1,2))


class Ball:
    
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        
a = Ball(5, 5, 1)
b = Ball(4, 4, 2)
c = Ball(-1, 4, 2)
d = Ball(4, 8, 2)
balls = [a, b, c, d]

def distance(a,b):
    return ((a.x-b.x)**2+(a.y-b.y)**2)**0.5

for b1 in balls:
    for b2 in balls:
        if b1 is not b2 and b1.r+b2.r >= distance(b1,b2):
            print(b1.x, b1.y, b2.x, b2.y)
#print(a.r)
#print(a.r)


     