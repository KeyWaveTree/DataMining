import numpy as np
import matplotlib.pyplot as plt

N = 10

x = np.array([i for i in range(N)])

data1 = np.random.normal(scale=0.1, size=(N))
print('data1')
print(data1)

data2 = np.random.normal(scale=1, size=(N))
print('data2')
print(data2)

print('data1 variance:', np.var(data1))

print('data2 variance:', np.var(data2))

plt.subplot(2, 1, 1)
plt.scatter(x, data1)
plt.ylim((-1, 1))
plt.axhline(np.mean(data1))

plt.subplot(2, 1, 2)
plt.scatter(x, data2)
plt.ylim((-1, 1))
plt.axhline(np.mean(data2))

plt.show()
