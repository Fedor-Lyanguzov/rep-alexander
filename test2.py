print('Hello world!')

x = 5
y = 6
point = {}
point['x'] = 5
point['y'] = 6
dictionary = {}
dictionary['apple'] = 'яблоко'

l = []
l.append(5)
l.append(6)
for i in range(100):
    l.append(i)
razn = []
for i in range(len(l)-1):
    razn.append(l[i+1] - l[i])
#l.append('apple')

print(razn)
