import numpy as np

x = np.arange(40).reshape(10, 4)
a = x[4, 3]
b = x[0:10:2, 0:4:2]

if __name__ == '__main__':
    print(a)
    print(b)