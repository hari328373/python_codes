
#combinations
import math

def iterables(size,input,K):
    Count = len(list(filter(lambda x: x == "a",input))) #lambda expression
    total = math.comb(size,K) #combinations
    withoutA = math.comb(size-Count, K)
    result = 1 - withoutA/total
    return "{0:.3f}".format(result) # decimal point value upto 3 decimals