# reverse a string
def rev(str):
    arr = list(str)
    for i in range(len(arr)):
        print(arr.pop())
    return(0)

def rev1(str):
    for c in range(len(str)):
        print(str[-1])
        str = str[0:-1]

# implement stack
class Stack():
    def __init__(self):
        self.stack = []

    def append(self, var):
        self.stack.append(var)
        return(0)

    def pop(self):
        return(self.stack.pop())

# convert decimal to binary
def dToB(num):
    ret_arr = []
    quotient = num
    while quotient != 0:
        rem = quotient % 2
        quotient = quotient//2
        ret_arr.append(rem)
    return(ret_arr[::-1])

# convert binary to decimal
def bToD(numB):
    ret_int = 0
    bPlace = 0
    while len(numB) != 0:
        ret_int += (2**bPlace)*numB.pop()
        bPlace += 1
    return(ret_int)


# convert decimal to hex
def dToH(num):
    ret_arr = []
    quotient = num
    ref = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    while quotient != 0:
        rem = quotient % 16
        quotient = quotient//16
        ret_arr.append(ref[rem])
    return(ret_arr[::-1])

def hToD(num):
    multiple = 0
    ret_int = 0
    ref = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']
    while len(num) > 0:
        ret_int += ref.index(num.pop())*(16**multiple)
        multiple += 1
    return(ret_int)



if __name__ == "__main__":
    print('testing rev')
    rev('abc')
    print('testing stack')
    test = Stack()
    test.append('a')
    test.append('b')
    print(test.pop())
    print('testing conversion')
    print(dToB(13))
    print(dToB(174))
    print(dToH(7562))
    print(dToH(79))
    print(bToD([1,1,0,1]))
    print(bToD([1,0,1,0,1,1,1,0]))
    print(hToD([1,'D',8,'A']))
    print(hToD([4,'F']))



#Find local maxima in array
