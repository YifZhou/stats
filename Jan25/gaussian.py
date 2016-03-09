#! /usr/bin/env python
from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('myggplot')
"""transform uniform to exponential
"""


def trans(x1, x2):
    y1 = np.sqrt(-2 * np.log(x1)) * np.cos(2 * np.pi * x2)
    y2 = np.sqrt(-2 * np.log(x1)) * np.sin(2 * np.pi * x2)
    return y1, y2


def gaussian(x):
    return 1 / np.sqrt(2 * np.pi) * np.exp(-x**2 / 2)

if __name__ == '__main__':
    length = 100000
    a = 0.5
    x1 = np.random.random(length)
    x2 = np.random.random(length)
    y1, y2 = trans(x1, x2)
    plt.close('all')
    nbin = 50
    bins = np.linspace(-5, 5, nbin)
    plt.hist(y1, bins=bins, normed=True)
    ysamp = np.linspace(-3, 3, 200)
    plt.plot(ysamp, gaussian(ysamp), lw=2)
    plt.xlabel('$y_1$')
    plt.ylabel('$P(y_1)$')
    plt.show()
