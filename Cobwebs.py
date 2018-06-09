# Cobwebs.py
# Nathan Greene
# Summer 2018
#
# Cobwebs are a method for finding fixed points, divergence, and cycles in
# maps, or one dimensional flows.  See Nonlinear Dynamics and Chaos by
# Steven Strogatz.  This script plots a cobweb for a given function f and
# seed x0 for a number of iterations.  Use caution; most functions diverge.

import math
import matplotlib.pyplot as plt

def main():
    cobwebs(lambda x : x ** 2 - 1, (1 + math.sqrt(5)) / 2 - 0.001, 100)

def cobwebs(f, x0 = 0.001, iters=0):
    """ Plot cobwebs on a given function f """
    # Point plots
    x, y = [], []
    for i in range(iters):
        if i == 0:
            x.append(x0)
        else:
            x.append(y[i - 1])
        y.append(f(x[i]))
    plt.plot(x, y, "ko")
    plt.plot(x, x, "bo")

    # Arrow plots
    for i in range(0, len(x) - 1):
        plt.arrow(x[i], x[i], 0, y[i] - x[i])       # Vertical
        plt.arrow(x[i], y[i], x[i + 1] - x[i], 0)   # Horizontal

    # Line plots
    d = 100
    xmin = min(x)
    xmax = max(x)
    x = [xmin * (1 - a / d) + a * xmax / d for a in range(d)]
    y = [f(xi) for xi in x]
    plt.plot(x, y, "k-")
    plt.plot(x, x, "b-")

    # Display cobweb plots
    plt.suptitle("Cobwebs: f (x) = x^2 - 1")
    plt.show()

main()
