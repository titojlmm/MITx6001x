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
plt.plot(mySamples, myLinear, label='linear')
plt.plot(mySamples, myQuadratic, label='quadratic')
plt.legend(loc = 'upper left')

plt.figure('cubic expo')
plt.clf()
plt.title('Cubic vs. Exponential')
plt.plot(mySamples, myCubic, label='cubic')
plt.plot(mySamples, myExponential, label='exponential')
plt.legend()
