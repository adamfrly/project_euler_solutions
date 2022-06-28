# Figure out the largest convex hole (convex hull without interior points) among a set of 500 pseudo randomly generated numbers

# NOT SOLVED

import numpy as np
import matplotlib.pyplot as plt


def create_points():
    s = [0] * 1001
    s[0] = 290797

    for n in range(1000):
        s[n+1] = (s[n] ** 2) % 50515093

    t = [(s[n] % 2000) - 1000 for n in range(len(s))]
    t.pop(0)

    return list(zip(*(iter(t),) * 2))


points = create_points()
x_list = [point[0] for point in points]
y_list = [point[1] for point in points]

x = np.array(x_list)
y = np.array(y_list)

plt.scatter(x,y)
plt.show()