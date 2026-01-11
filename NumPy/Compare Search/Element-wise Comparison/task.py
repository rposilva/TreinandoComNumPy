import numpy as np

a = np.arange(20).reshape(4, 5)
# [0,1,2,3,4]
# [5,6,7,8,9]
# [10,11,12,13,14]
# [15,16,17,18,19]
b = np.arange(0, 25, 6).reshape(5,)
compare_a_b = np.equal(a, b)


if __name__ == '__main__':
    print(a)
    print(b)
    print(np.array_equal(compare_a_b, np.array([[True, False, False, False, False],
                                                [False, True, False, False, False],
                                                [False, False, True, False, False],
                                                [False, False, False, True, False]])))

