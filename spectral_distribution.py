import numpy as np
import matplotlib.pyplot as plt
import random

#calculates spectral radiance as a function of wavelength, temperature
def planck(wavelength,temp):
    h = 6.626E-34
    c = 3.0E8
    k = 1.38E-23
    return((2*h*c**2/(wavelength*1E-9)**5) * (1/(np.exp(h*c/(k*temp*wavelength*1E-9))-1)))

#spectral radiance distributions for stars of 4 surface temperatures (K)
temp = 3000

#filling random distribution over range of 0 nm to 2000nm based on planck distribution
lambdas = np.linspace(1,2000,2000)
#distributions for each star surface temperature
distributions = []
for i in range(len(lambdas)):
    distributions.append(planck(lambdas[i],temp))

#plt.plot(lambdas,distributions)

#adjusting into array and normalizing
a = np.asarray(distributions)
b= np.sum(a)
c = a/b

#random selections based on normalized planck distribution
data = random.choices(lambdas,c,k=30000)

#plotting as histogram
n, b, patches = plt.hist(data, bins=25, alpha=0.7 ,rwidth=0.95, density = True, facecolor = "blue")
plt.xlabel('wavelength (nm)')
plt.ylabel('bin density')
plt.title('30000K surface temperature simulated spectrum')
plt.grid(axis='y', alpha=0.75)
#plt.savefig('t3000.pdf')

bin_max = np.where(n == n.max())

print ('maximum wavelength: ', b[bin_max][0], 'nm')

