# -*- coding: utf-8 -*-
import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.figure('lin quad')
plt.clf()
plt.title('Linear vs. Quadratic')
plt.subplot(211)
plt.ylim(0, 900)
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
plt.legend(loc = 'upper left')
plt.subplot(212)
plt.ylim(0, 900)
plt.plot(mySamples, myQuadratic, 'r', label='quadratic', linewidth=3.0)
plt.legend(loc = 'upper left')

plt.figure('cubic expo')
plt.clf()
plt.title('Cubic vs. Exponential')
plt.subplot(121)
plt.ylim(0, 140000)
plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=4.0)
plt.legend(loc = 'upper left')
plt.subplot(122)
plt.ylim(0, 140000)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=5.0)
plt.legend(loc = 'upper left')
