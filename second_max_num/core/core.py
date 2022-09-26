#find the score of the runner-up


def sec_max(arr):
    m = sorted(list(set(arr)))
    return m[-2]