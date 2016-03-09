from __future__ import print_function, division
import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def gaussian(x, x0, sigma):
    return 1 / np.sqrt(2 * np.pi * sigma) * np.exp(-(x - x0)**2 / (2 * sigma))


def var_gaussian(x):
    return np.exp(-x**2 / 2)


def pmInt(x_low, x_high, dx):
    """poor man's integrator for Gaussian function
basically just sum up"""
    x = np.linspace(x_low, x_high, (x_high - x_low) / dx)
    g_x = var_gaussian(x)
    return dx / np.sqrt(2 * np.pi) * (sum(g_x) - 0.5 * (g_x[0] + g_x[-1]))

if __name__ == '__main__':
    for i in xrange(1, 6):
        dx = 1 / 4096 / 2**i
        inte = pmInt(-i, i, dx)
        inte2 = quad(var_gaussian, -i, i) / np.sqrt(2 * np.pi)
        print('{0:d}$sigma$, {1:.9f}, {2:.9f} {3:.9f} {4:.9f}'.format(
            i, inte, 1 - inte, inte2[0], 1 - inte2[0]))
    # inteList = []
    # nList = 4096 * np.arange(1, 100)
    # for N in nList:
    #     dx = 1 / N
    #     inteList.append(pmInt(-5, 5, dx))

    # plt.close('all')
    # plt.plot(nList, inteList)
    # plt.show()
