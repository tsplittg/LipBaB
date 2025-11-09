import numpy as np
import matplotlib.pyplot as plt
from scipy.special import expit

plot_points = np.linspace(-5,5, 100)
sigmoid_values = expit(plot_points)
fig, ax = plt.subplots(figsize = (20,12))
ax.plot(plot_points, sigmoid_values, linewidth = 6, label = "Sigmoid function")
ax.set_xlabel("x", fontsize = 20)
ax.set_ylabel("y", fontsize = 20, rotation = 0)
ax.set_ylim(0,1)
ax.legend(fontsize = 25)
fig.savefig("Lipschitz_sigmoid_illustration.pdf")
ax.plot(plot_points, plot_points/4+0.5, linewidth = 6, c="red", label = "Maximum derivative: m = 1/4")
ax.legend(fontsize = 25)
fig.savefig("Lipschitz_sigmoid_illustration_with_derivative.pdf")



fig, ax = plt.subplots(figsize = (20,12))
ax.plot(plot_points, plot_points, linewidth = 6, label = "Linear function")
ax.set_xlabel("x", fontsize = 20)
ax.set_ylabel("y", fontsize = 20, rotation = 0)
ax.legend(fontsize = 25)
fig.savefig("Lipschitz_linear_illustration.pdf")