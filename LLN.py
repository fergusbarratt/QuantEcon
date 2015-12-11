import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import matplotlib.pyplot as plt


def y2(y1, y0, a, b, c, sigma):
    return a+b*y1+c*y0+sigma*np.random.standard_normal()

def y4(y3, y2, y1, y0, a, b, c, d, e, sigma):
    return a+b*y3+c*y2+d*y1+e*y0+sigma*np.random.standard_normal()


def evolve(func, time, prevs=[1, 1], params=[1.1, 0.8, -0.8, 0.02], timestep=1):
    func(*prevs+params)
    for i in range(0, time, timestep):
        app = func(*prevs+params)
        del prevs[-1]
        prevs.insert(0, app)
        yield app

f, ax1 = plt.subplots(1, 1)
realizations = 6
for _ in range(realizations):
    realization = list(evolve(y4, 200, [1, 1, 1, 1], [0, 0.5, -0.2, -1, 0.5, 10]))
    ax1.plot(realization)
ax1.set_title("realizations")
ax1.set_xlabel("time")


plt.show()

