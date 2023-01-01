import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

m1, c1 = 0.1, 10
m2, c2 = 2.0, 3

x = np.linspace(0, 10)

plt.plot(x, x * m1 + c1, 'red')
plt.plot(x, x * m2 + c2, 'green')



xi = (c1 - c2) / (m2 - m1)
yi = m1 * xi + c1

plt.axvline(x=xi, color='gray', linestyle='--')
plt.axhline(y=yi, color='gray', linestyle='--')

plt.scatter(xi, yi, color='black')

plt.show()

