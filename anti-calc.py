import random
import operator

numbers = [ x for x in range (-100,101) ]
znaki = [ "+","-","*" ]
numbers2 = [ x for x in range (-100,101) ]

def plus(a, b):
    return a+b

op_map = { "+": plus,
           "-": operator.sub,
           "*": operator.mul
    }


def simple_addition():
    a = random.randint(1,8)
    b = random.randint(1, 9-a)
    c = a + b
    return a, b, c

addition_types = { "simple": simple_addition,}
#                   "over_ten": over_ten_addition,
#                   "hard": hard_addition}

def addition(t):
    return addition_types[t]()
    
h = False
results = []
for x in range(10):
    a,b,c = addition("simple")
    results.append(c)
    op = "+"
##    a = random.choice(numbers)
##    b = random.choice(numbers)
##    op = random.choice(znaki)
##    c = op_map[op](a,b)
    print(a,op,b,"=",c)
print(sorted(results))
