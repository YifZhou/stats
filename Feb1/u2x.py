#! /usr/bin/env python
from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
"""u to x distribution
"""
u0 = 1.0
usig = [0.1, 0.4, 0.5, 2.0]
plt.close('all')
for i, usig_i in enumerate(usig):
    udistr = np.random.normal(loc=u0, scale=usig_i, size=1000000)
    xdistr = udistr**2
    fig = plt.figure(i)
    ax = fig.add_subplot(111)
    ax.hist(xdistr, bins=500, normed=True)
    ax.set_title('$u_\sigma=${0:.1f}'.format(usig_i))

plt.show()
