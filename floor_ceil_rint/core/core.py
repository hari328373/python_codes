import numpy as np


def floors(arr):
    array = np.array(arr)
    np.set_printoptions(legacy='1.13')
    return np.floor(array)
def ceils(arr):
    array = np.array(arr)
    return np.ceil(array)
def rints(arr):
    array = np.array(arr)
    return np.rint(array)

#arr=[1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9]
#k= floors(arr)
