from util import *

with open("01.txt", 'r') as file:
    ileft, iright = zip(*[map(int, line.split()) for line in file])

# p.1
right, left = list(iright), list(ileft)
dists = []
for i in range(len(left)):
    lmin = min(left)
    left.remove(lmin)
    rmin = min(right)
    right.remove(rmin)
    dists.append(abs(rmin-lmin))
print("Distance:", sum(dists))

# p.2
right, left = list(iright), list(ileft)
ramount = {}
for r in right: 
    ramount[r] = right.count(r)
total = sum(l * ramount.get(l, 0) for l in left)
print("Total:", total)
