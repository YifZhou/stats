from __future__ import print_function, division
import numpy as np
from numpy import random
from scipy.integrate import quad
import matplotlib.pyplot as plt
plt.style.use('ggplot')


def two_step_method(c0, ymin, ymax, bins=1024, N=2**16, P_N=64):
    ymid = (ymax + ymin) / 2
    yList = random.normal(ymid, size=N)
    # P: probability density of each bin
    # bins: bin edges
    P, bins = np.histogram(yList, bins=bins, normed=True)
    Pmax = np.max(P)  # maximum probability denstiy
    dbin = bins[1] - bins[0]  # bin size
    Pgrid = np.linspace(0, Pmax, P_N)  # a grid for P
    C = np.zeros(P_N)  # cumulative probability distribution
    for i, p in enumerate(Pgrid):
        C[i] = np.sum(P[P > p]) * dbin

    # find corrsponding y
    high_i = np.argwhere(C < c0)[0]
    low_i = np.argwhere(C >= c0)[-1]
    P_high = Pgrid[high_i]
    P_low = Pgrid[low_i]
    bin_between = np.argwhere(P > P_high)
    ylow = bins[bin_between[0] - 1]
    yhigh = bins[bin_between[-1] + 1]
    return ylow, yhigh


if __name__ == '__main__':
    plt.close('all')
    two_step_method(0.68, 0, 5, bins=512, N=2**16, P_N=64)
    plt.show()
