import random
from math import cos, sin, radians, sqrt
import numpy as np
import matplotlib.pyplot as plt


angle = [90,180,270,360]
lst1 = []
lst2 = []

def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step1 = np.random.uniform(0,1)
        #step1 = np.random.choice([0,0.5,1])
        #step2 = radians(np.random.choice(angle)
        step2 = radians(random.randrange(360))
        if sqrt(((x*step1*cos(step2))**2) + ((y*step1*sin(step2))**2)) <= 100:
            x = x + step1*cos(step2)
            y = y + step1*sin(step2)
        else:
            x = x
            y = y
        lst1.append(x)
        lst2.append(y)
random_walk(10000)
#print(lst1)
#print(lst2)

plt.xlim(-100,100)
plt.ylim(-100,100)
c = plt.Circle((0,0), 100, fill = False)
uzair = plt.gcf().gca()
uzair.add_artist(c)
plt.plot(lst1,lst2)
plt.show()
