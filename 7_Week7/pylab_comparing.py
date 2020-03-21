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

plt.figure('lin')
plt.clf()
plt.title('Linear')
plt.ylim(0,1000)
plt.plot(mySamples, myLinear)
plt.figure('quad')
plt.clf()
plt.title('Quadratic')
plt.ylim(0,1000)
plt.plot(mySamples, myQuadratic)
plt.figure('cubic')
plt.clf()
plt.title('Cubic')
plt.ylim(0,1000)
plt.plot(mySamples, myCubic)
plt.figure('expo')
plt.clf()
plt.title('Exponential')
plt.ylim(0,1000)
plt.plot(mySamples, myExponential)
