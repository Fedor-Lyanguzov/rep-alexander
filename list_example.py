print('H w')
x = [1,2,3,4,5]
y = [6,7,8,9,10]
z = []

my_list = []
for s in input().split():
    my_list.append(int(s))
print(sum(my_list)/len(my_list))    
"""
for i in range(5):
    z.append (x[i] - y[i])

print (z) 
"""
"""
print(list(zip(x,y)))
z = [ a-b for a,b in zip(x,y) ]
print(z)
"""
