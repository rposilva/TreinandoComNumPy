from numpy import linalg
import numpy as np
import matplotlib.pyplot as plt

img = plt.imread('horse.jpg')

img_rescaled = img / 255

img_array_transposed = np.transpose(img_rescaled, (2, 0, 1))
U, s, Vt = linalg.svd(img_array_transposed)

Sigma = np.zeros_like(img_array_transposed)
for i in range(3):
    np.fill_diagonal(Sigma[i], s[i])

reconstructed = U @ Sigma @ Vt


if __name__ == '__main__':
    print('Shape of the reconstructed image array: ', reconstructed.shape)
    print('Minimum value in the reconstructed image array: ', reconstructed.min())
    print('Maximum value in the reconstructed image array: ', reconstructed.max())
    # This assertion will fail if your reconstruction isn't close to the original:
    np.testing.assert_array_almost_equal(reconstructed, img_array_transposed)

    reconstructed = np.clip(reconstructed, 0, 1)
    plt.imshow(np.transpose(reconstructed, (1, 2, 0)))
    plt.show()

