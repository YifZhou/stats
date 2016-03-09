#! /usr/bin/env python
from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('myggplot')
"""transform uniform to exponential
"""


def Gauss(length, y0=0, sigma=1):
    x1 = np.random.random(length)
    x2 = np.random.random(length)
    y1 = np.sqrt(-2 * np.log(x1)) * np.cos(2 * np.pi * x2)
    # y2 = np.sqrt(-2 * np.log(x1)) * np.sin(2 * np.pi * x2)
    return y1 * sigma + y0


def MaxDist(length, sig1=1, sig2=1, sig3=3):
    v1 = Gauss(length, sigma=sig1)
    v2 = Gauss(length, sigma=sig2)
    v3 = Gauss(length, sigma=sig3)
    return np.sqrt(v1 * v1 + v2 * v2 + v3 * v3)


if __name__ == '__main__':
    length = 100000
    v = MaxDist(length, 10, 5, 2.5)
    plt.close('all')
    nbin = 50
    bins = np.linspace(0, 10, nbin)
    plt.hist(v, bins=nbin, normed=True)
    # ysamp = np.linspace(-3, 3, 200)
    # plt.plot(ysamp, gaussian(ysamp), lw=2)
    plt.xlabel('$v$')
    plt.ylabel('$P(v)$')
    plt.show()
