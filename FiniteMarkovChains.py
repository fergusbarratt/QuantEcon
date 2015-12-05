'''quantecon notetaking'''

import numpy as np
import quantecon as qe
import matplotlib.pyplot as plt
P1 = np.array([[0.971, 0.029, 0], [0.145, 0.778, 0.077], [0, 0.508, 0.492]])
P2 = np.array([[0.4, 0.6], [0.2, 0.8]])


def mc_sample_path(P, init=0, sample_size=1000):
    P = np.asarray(P)
    X = np.empty(sample_size, dtype=int)
    X[0] = init
    n = len(P)
    P_dist = [qe.DiscreteRV(P[i, :]) for i in range(n)]
    for t in range(sample_size - 1):
        X[t+1] = P_dist[X[t]].draw()
    return X

mc1 = qe.MarkovChain(P1)
# Y = mc_sample_path(P2, sample_size=100)
Y = mc1.simulate(ts_length=100)
X = np.ones_like(Y)
print(np.mean(Y == 0))
for i in enumerate(X):
    X[i[0]] = i[0]
fig, ax = plt.subplots()
rects = ax.bar(X, Y)
plt.show()
