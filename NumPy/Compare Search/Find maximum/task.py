import numpy as np

data = np.loadtxt('data.csv', delimiter=',', dtype=np.int64) # Import data
maxima = np.argmax(data, axis=1).reshape(-1, 1) # Find indices of maximum values in each row
result = np.take_along_axis(data, maxima, axis=1) # Extract the maximum elements from each row

if __name__ == '__main__':
    print('Dados \n', data)
    print('\n')
    print('Shape do data:', data.shape)
    print('Sahpe do maxima:', maxima.shape)
    print('\nResultado da Máxima\n', result)
