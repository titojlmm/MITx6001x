# -*- coding: utf-8 -*-
import pylab as plt

mySamples = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myCubic.append(i**3)
    myExponential.append(1.5**i)

plt.figure('cubic expo linear')
plt.clf()
plt.title('Cubic vs. Exponential (Linear)')
plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=2.0)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=4.0)
plt.legend()

plt.figure('cubic expo log')
plt.clf()
plt.title('Cubic vs. Exponential (Logaritmic)')
plt.plot(mySamples, myCubic, 'g--', label='cubic', linewidth=2.0)
plt.plot(mySamples, myExponential, 'r', label='exponential', linewidth=4.0)
plt.yscale('log')
plt.legend()
