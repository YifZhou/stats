#! /usr/bin/env python
from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
"""transform uniform to exponential
"""


def trans(x, a):
    return -a * np.log(x)


def exponential(y, a):
    return 1 / a * np.exp(-y / a)

if __name__ == '__main__':
    length = 100000
    a = 0.5
    x = np.random.random(length)
    y = trans(x, a)
    plt.close('all')
    plt.hist(y, bins=25, normed=True)
    samp_y = np.linspace(0.001, 5, 100)
    plt.plot(samp_y, exponential(samp_y, a))
    plt.xlabel('$y$')
    plt.ylabel('$P(y)$')
    plt.show()
