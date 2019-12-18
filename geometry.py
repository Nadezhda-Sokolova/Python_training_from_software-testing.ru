
from geom2d.point import *

#l = [Point(i, i*i) for i in range(-5,6) ]

l = list(map(lambda i: Point(i, i*i), range (-5,6)))

print(l)

#l2 = list(map(lambda p: Point(p.x, -p.y), l))
#l2 = list(filter(lambda p: p.x >0, l))
l2 = list(filter(lambda p: p.x%2 == 0, l))


print(l2)
