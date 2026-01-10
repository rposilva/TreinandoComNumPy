import numpy as np


def reshape_transpose(start, stop, step=1):
    arr = np.arange(start, stop, step) # Create a 1D array using arange function
    arr_2d = arr.reshape(1, -1) # Reshape the 1D array so that you can transpose it
    return arr_2d.T # Return the transposed array


if __name__ == '__main__':
    print(reshape_transpose(1, 100, 10))
    print(reshape_transpose(0, 5))
