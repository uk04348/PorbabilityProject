import random
import numpy as np
import matplotlib.pyplot as plt

pright1 = float(input("Enter prob of right of first= "))
pleft1 = float(input("Enter prob of left of first = "))
pnomove1 = 1 - (pright1 + pleft1)

pright2 = float(input("Enter prob of right of second = "))
pleft2 = float(input("Enter prob of left of second = "))
pnomove2 = 1 - (pright2 + pleft2)

probabilitylist1 = [pnomove1,pleft1,pright1]
probabilitylist2 = [pnomove2,pleft2,pright2]

lst1 = []
lst2 = []
n = 3
def random_walk(n):
    steps = 0
    dist1 = random.randint(-3,0)
    dist2 = random.randint(0,3)
    lst1.append(abs(dist1) + abs(dist2))
    while True:
        steps+=1
        step1 = np.random.choice([0,-1,1],p = probabilitylist1)
        step2 = np.random.choice([0,-1,1],p = probabilitylist2)
        if step1 == -1:
            dist1 -= 1
        elif step1 == 1:
            dist1 += 1
        if step2 == -1:
            dist2 -= 1
        elif step2 == 1:
            dist2 += 1
        if dist1 == dist2:
            return steps
for i in range(n):
    lst2.append(random_walk(n))
print(lst2)



plt.xlabel("Distance")
plt.ylabel("Probability")
plt.plot(lst2, lst1)
plt.show()
