import numpy as np

rng = np.random.default_rng()

x = np.arange(10)
x = x.reshape(10, 1)# TODO: modify x so that the print statement does not throw an exception
y = np.ones(7)

w = rng.integers(2, size=(4, 3))
w = w.reshape(3, 4)# TODO: modify w so that the print statement does not throw an exception
z = np.ones((3, 4))

if __name__ == '__main__':
    print('Array x:\n', x)
    print('Array y:\n', y)
    print('Array x + y:\n', x + y)
    print('Array z:\n', z)
    print('Array w:\n', w)
    print('Array z * w:\n', z * w)
