#numpy contains linalg as sub_module
#linalg.det to perform determinant function

import numpy as np
def linear_algebra(arr):
    return np.linalg.det(arr).round(2)


