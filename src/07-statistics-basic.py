import numpy as np
import matplotlib.pyplot as plt

N = 10

x = np.array([i for i in range(N)])

data = np.random.randint(10, size=N)
print('data')
print(data)

print('mean:', np.mean(data))
print('deviation:', data - np.mean(data))
print('variance:', np.var(data))
print('standard deviation:', np.std(data))

plt.figure(0)
plt.scatter(x, data)
plt.axhline(np.mean(data))
plt.show()
