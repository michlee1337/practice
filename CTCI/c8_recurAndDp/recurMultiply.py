import math

def _isPrime(in_int):
    '''
    input: int
    returns: bool
    '''
    for n in range(math.sqrt(in_int)):
        if in_int%n == 0:
            return(False)
    return(True)

def smallestDivisor(in_int):
    '''
    input: int
    returns: int

    -1 if can't be found
    '''
    for n in range(2,in_int):
        if in_int%n == 0:
            return(n)
    return(-1)

def recur_multiply(int1, int2):
    '''
    input: int,int
    returns: int
    '''
    mult_table = {}
    prime_list = []

    # get smaller int
    if int1 < int2:
        small_int = int1
        big_int = int2
    else:
        small_int = int2
        big_int = int1

    # break down big int into primes

    # base case, a prime
    while not _isPrime(big_int):
        # aw man how do i do this
        mult_table[smallestDivisor(in_int)] = big_int
        # try dividing from 2 up
    # add it by itself x times if x is a prime
