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
plt.plot(mySamples, myLinear, 'b-', label='linear', linewidth=2.0)
plt.plot(mySamples, myQuadratic, 'ro', label='quadratic', linewidth=3.0)
plt.legend(loc = 'upper left')

plt.figure('cubic expo')
plt.clf()
plt.title('Cubic vs. Exponential')
plt.plot(mySamples, myCubic, 'g^', label='cubic', linewidth=4.0)
plt.plot(mySamples, myExponential, 'r--', label='exponential', linewidth=5.0)
plt.legend()
