#! /usr/bin/env python
from __future__ import print_function, division
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('paper')
"""Intensity to magnitude, see distribution difference
"""


def I2mag(I):
    return -2.5 * np.log10(I)


def gauss(x, mean, sig):
    return 1 / np.sqrt(2 * np.pi) / sig * np.exp(-(x - mean)**2 / (2 * sig**2))

if __name__ == '__main__':
    sigI = 0.5
    I0 = 1.0
    I = np.random.normal(loc=I0, scale=sigI, size=1000000)
    mag = I2mag(I)
    mag = mag[~np.isnan(mag)]
    plt.close('all')
    fig = plt.figure(figsize=(10, 6))
    axI = fig.add_subplot(121)
    axI.hist(I, bins=40, normed=True)
    xI = np.linspace(I0 - 3 * sigI, I0 + 3 * sigI, 1000)
    axI.plot(xI, gauss(xI, I0, sigI), lw=2)
    axI.plot()
    sigMag = 2.5 / np.log(10) * (sigI / I0)
    meanMag = -2.5 * np.log10(I0)
    axMag = fig.add_subplot(122)
    axMag.hist(mag, bins=np.linspace(meanMag - 4 * sigMag,
                                     meanMag + 4 * sigMag, 40), normed=True,
               )
    xMag = np.linspace(meanMag - 4 * sigMag, meanMag + 4 * sigMag, 1000)
    axMag.plot(xMag, gauss(xMag, meanMag, sigMag), lw=2)
    print('I={0}, sigI={1}'.format(I0, sigI))
    print('Propagated Mean Mag: {0:.3f}, MC Mean Mag: {1:.4f}'.format(
        meanMag, np.mean(mag)))
    print('Propagated Sig Mag: {0:.3f}, MC Sig Mag: {1:.4f}'.format(
        sigMag, np.std(mag))
    plt.show()
