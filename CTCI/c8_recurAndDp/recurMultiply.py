
# helper: multiply int by multiplier
### keeps original params of main the same
def multiply_by(int, multiplier):
    '''
    input: int,int
    returns: int
    '''
    res = int

    # base case: if multiplier is 1, return int
    if multiplier == 1:
        pass

    # base case: if the multiplier is 2, left shift
    elif multiplier == 2:
        res = res << 1

    # else: left shift and deduct 2 from multiplier, check again
    while multiplier >= 2:
        res = res << 1
        multiplier -= 2

    res += multiply_by(int, multiplier)
    return(res)

def recur_multiply(int1, int2):
    '''
    input: int,int
    returns: int
    '''

    # set larger int as multiplier
    if int1 < int2:
        small_int = int1
        big_int = int2
    else:
        small_int = int2
        big_int = int1

    res = multiply_by(small_int, big_int)
    return(res)

if __name__=="__main__":
    int1 = int(input("int 1: "))
    int2 = int(input("int 2: "))
    print(recur_multiply(int1,int2))
