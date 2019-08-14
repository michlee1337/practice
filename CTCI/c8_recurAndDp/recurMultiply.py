
'''
import math

def _isPrime(in_int):
    for n in range(math.sqrt(in_int)):
        if in_int%n == 0:
            return(False)
    return(True)

def smallestDivisor(in_int):
    for n in range(2,in_int):
        if in_int%n == 0:
            return(n)
    return(-1)
'''


def recur_multiply(int1, int2):
    '''
    input: int,int
    returns: int
    '''

    # find closest exponent - is that the right word - of 2
    # add and subtract difference
    exponents = 0

    # get smaller int
    if int1 < int2:
        small_int = int1
        big_int = int2
    else:
        small_int = int2
        big_int = int1

    # break down big int into primes
    # count number of powers of 2 that fit into big int
    while big_int % 2 == 0:
        exponents += 1
        big_int = big_int >> 1

    # multiply small int by that power
    sol = small_int << exponents

    # then add the number of times of remaining big_int
    for _ in range(big_int-1):
        sol += small_int
    return(sol)

if __name__=="__main__":
    int1 = int(input("int 1: "))
    int2 = int(input("int 2: "))
    print(recur_multiply(int1,int2))
