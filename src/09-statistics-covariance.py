import numpy as np
import matplotlib.pyplot as plt

N = 100

x = np.random.normal(scale=10, size=(N))

a = 2
b = 5
noise = np.random.normal(scale=2, size=(N))
data1 = a * x + b + noise

a = -5000
b = -60000
noise = np.random.normal(scale=50000, size=(N))
data2 = a * x + b + noise

data3 = np.random.normal(scale=0.1, size=(N))

print('data1 covariance:', np.cov(x, data1, ddof=0)[0][1])
print('data2 covariance:', np.cov(x, data2, ddof=0)[0][1])
print('data3 covariance:', np.cov(x, data3, ddof=0)[0][1])

print('data1 correlation coefficient:', np.corrcoef(x, data1)[0][1])
print('data2 correlation coefficient:', np.corrcoef(x, data2)[0][1])
print('data3 correlation coefficient:', np.corrcoef(x, data3)[0][1])

plt.subplot(2, 2, 1)
plt.scatter(x, data1)
plt.title('data1')

plt.subplot(2, 2, 2)
plt.scatter(x, data2)
plt.title('data2')

plt.subplot(2, 1, 2)
plt.scatter(x, data3)
plt.title('data3')

plt.show()
