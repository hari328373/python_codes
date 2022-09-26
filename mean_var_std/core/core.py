# arithmetic mean, variance, standard deviation
# axis=0--> colmns
# axis=1-->rows

import numpy as np


def arr_mean(arr):
    return np.mean(arr, axis=1)  # return arithmetic mean


def arr_var(arr):
    return np.var(arr, axis=0)  # variance


def arr_std(arr):
    k = np.std(arr, axis=None)
    return k.round(11)  # standard deviation
