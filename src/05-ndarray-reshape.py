import numpy as np

data = [[str(i) + str(j) for j in range(10)] for i in range(10)]
data = np.array(data)
print('data')
print(data)

a = data[:, 0]
print('data[:, 0]')
print(a.shape)
print(a)

a = a.reshape(5, 2)
print('a.reshape(5, 2)')
print(a.shape)
print(a)

a = a.reshape(-1, 1)
print('a.reshape(-1, 1)')
print(a.shape)
print(a)
