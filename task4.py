import random
import numpy as np
import matplotlib.pyplot as plt

pright = float(input("Enter prob of right = "))
pleft = float(input("Enter prob of left = "))
pnomove = 1 - (pright+pleft)
probabilitylist = [pnomove,pleft,pright]
lst2 = []
n = 3
def random_walk(n):
    x = 0
    for i in range(n):
        s = np.random.uniform(0,1)
        step = np.random.choice([0,-1,1],p = probabilitylist)
        if step == -1:
            x = x - s
        elif step == 1:
            x = x + s
        else:
            continue
    return x
for i in range(n):
    lst2.append(random_walk(n))
print(lst2)



plt.xlabel("Distance")
plt.ylabel("Probability")
plt.plot(lst2,probabilitylist)
plt.show()
