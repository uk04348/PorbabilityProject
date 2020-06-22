import random
from math import cos, sin, radians, sqrt
import numpy as np
import matplotlib.pyplot as plt


angle = [90,180,270,360]
lst1 = []
lst2 = []
lst3 = []
lst4 = []

def random_walk(n):
    count = 0
    x1 = random.randint(2,80)
    y1 = random.randint(2,60)
    x2 = random.randint(2,80)
    y2 = random.randint(2,60)
    for i in range(n):
        times = n
        count+=1
        step1 = np.random.choice([0,0.5,1])
        step2 = radians(random.randrange(360))
        step3 = np.random.choice([0,0.5,1])
        step4 = radians(random.randrange(360))
        if sqrt(((x1*step1*cos(step2))**2) + ((y1*step1*sin(step2))**2)) <= 100:
            x1 = x1 + step1*cos(step2)
            y1 = y1 + step1*sin(step2)
        else:
            x1 = x1
            y1 = y1
        if sqrt(((x2*step1*cos(step2))**2) + ((y2*step1*sin(step2))**2)) <= 100:
            x2 = x2 + step3*cos(step4)
            y2 = y2 + step3*sin(step4)
        else:
            x2 = x2
            y2 = y2
            
        if (sqrt((x2-x1)**2+(y2-y1)**2)) < 1:
            break
        lst1.append(x1)
        lst2.append(x2)
        lst3.append(y1)
        lst4.append(y2)
    print(count/times)


random_walk(10000)
plt.plot(lst1,lst2)
plt.plot(lst3,lst4)

plt.xlim(-100,100)
plt.ylim(-100,100)
c = plt.Circle((0,0), 100, fill = False)
uzair = plt.gcf().gca()
uzair.add_artist(c)

plt.show()
