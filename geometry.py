
from geom2d.point import *

l = [Point(i, i*i) for i in range(-5,6) ]

for i in range(-5,6):
    l.append(Point(i, i*i))

print(l)

l2 = []

for el in l:
    l2.append(Point(el.x, -el.y))

for el in l2:
    print(el)



