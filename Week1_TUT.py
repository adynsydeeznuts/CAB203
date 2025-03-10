def divisible(a, b):
    print(b % a == 0)

import math
def baseTwo(base, exp):
    print(math.log(base ** exp, 2))

def minBit(addresses):
    print(math.pow(2, baseTwo(addresses, 1)))

minBit(100)
    


