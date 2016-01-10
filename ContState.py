import numpy as np
import matplotlib.pyplot as plt

mean = np.array([0.2, -0.2])
cov = np.array([[0.4, 0.3], [0.3, 0.45]])

def re_param(guess, mean, G, Sig, R):
    re_mean = mean + Sig.dot(np.transpose(G)).dot((G.dot(Sig.dot(np.transpose(G)))) + R)

X = np.random.multivariate_normal(mean, cov, 1000)
plt.scatter(X[:, 0], X[:, 1])
plt.show()
