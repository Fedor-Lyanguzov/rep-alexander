import hotncold

number = 5

inp = [ (a,b) for a in range(10) for b in range(10) ]

for a,b in inp:
    print(a,b,hotncold.comparison(number,a,b))
