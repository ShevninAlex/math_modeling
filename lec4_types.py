def changer(a, b):
    a = 2
    b[0] = 'good'

x = 10
l = [1, 2]

changer(x, l)

print(x)
print(l)

l = [1, 2]
changer(x, l[:])

print(l)

x = 3
y =4
z = complex(x,y)
print(z)

w = complex(y, x)

print (z + w)

t = (1, 4, 5)
print(t)
print(t[0])
#t[0] = 3 - ошибка

d = {'al':4, 4:'al', 'str':'Hello'}
print(d['al'])
print(d[4])
print(d['str'])

d['str'] = 'good'
print(d)