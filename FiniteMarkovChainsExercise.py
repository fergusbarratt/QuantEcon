import numpy as np
import quantecon as qe
import matplotlib.pyplot as plt

alpha = 0.1
beta = 0.1
p = beta/(alpha+beta)


def X_bar(n, series):
    return (1/n) * np.sum(
        list(filter(lambda x: 1 if x == 1. else 0, series[0:n])))

P = np.array([[1-alpha, alpha], [beta, 1-beta]])
mc = qe.MarkovChain(P)

series1 = mc.simulate(ts_length=10000)
t_series = np.ones_like(series1)
for i in enumerate(t_series):
    t_series[i[0]] = i[0]+1

plots = 5
seriess = [mc.simulate(ts_length=10000) for i in range(plots)]
dists = [[X_bar(n, series) - p for n in t_series] for series in seriess]

for i in range(plots):
    plt.plot(t_series, dists[i])
plt.show()
