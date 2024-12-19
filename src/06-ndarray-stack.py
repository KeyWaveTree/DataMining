import numpy as np

data = [[str(i) + str(j) for j in range(10)] for i in range(10)]
data = np.array(data)

a = data[1:3, 2:5]
print('a = data[1:3, 2:5]')
print(a)

b = data[5:7, 7:10]
print('b = data[5:7, 7:10]')
print(b)

c = np.hstack((a, b))
print('np.hstack((a, b))')
print(c)

c = np.vstack((a, b))
print('np.vstack((a, b))')
print(c)
