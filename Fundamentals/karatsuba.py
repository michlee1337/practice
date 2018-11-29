def basicMultiplication(a,b):
    # multiply the larger number by the smaller number

    # cast into list to make life hard
    int1 = [int(i) for i in str(max(a,b))]
    int2 = [int(i) for i in str(min(a,b))]
    partials = []
    # for each digit in smaller number
    pos = 0
    for i in int2[::-1]:
        # compute a partial product and store it
        partial = []
        carry = 0
        # for each digit in larger number
        for j in int1[::-1]:
            # add the singles to the left of partial
            partial.insert(0,(carry + (i*j)) % 10)
            # store whatever is left to be carried to the next multiplication
            carry = ((i*j) + carry)// 10
        # insert any additional numbers to the partial
        if carry != 0:
            partial.insert(0,carry)
        # pad with 0s
        for x in range(pos):
            partial.append(0)
        # store partial
        partials.append(partial)
        pos += 1
    # add all partial products

    # make all partials same length by padding 0s
    standLen = max([len(i) for i in partials])

    for p in partials:
        for x in range(standLen - len(p)):
            p.insert(0,0)

    # add each element in partials from the last to first index
    res = [0] * standLen
    for i in range(standLen-1,-1,-1):
        for p in partials:
            res[i] += p[i]
    # check for carry values
    carry = 0
    for p in range(len(res)-1,-1,-1):
        cur = res[p]
        res[p] = (cur + carry) % 10
        carry = (cur + carry) // 10
    return(res)

#print(basicMultiplication(9,2))
#print(basicMultiplication(3841,24165))

# karasuba method
def karasuba(int1,int2):
    # base case: if both len 1, return simple multiplication
    int1 = [int(c) for c in str(int1)]
    int2 = [int(c) for c in str(int2)]
    print(int1,int2)
    if len(int1) == 1 and len(int2) == 1:
        return(int1[0] * int2[0])
    # recursively iterate
    else:
        print(int1,int2)
        int1_mid = len(int1)//2
        int2_mid = len(int2)//2
        a = int1[0:int1_mid]
        b = int1[int1_mid:len(int1)]
        c = int2[0:int2_mid]
        d = int2[int2_mid:len(int2)]
        ac = karasuba(a,c)
        bd = karasuba(b,d)
        abcd = karasuba([int(i) for i in str(int(''.join(map(str,a)))+int(''.join(map(str,b))))],[int(j) for j in str(int(''.join(map(str,c)))+int(''.join(map(str,d))))])
        print(abcd)
        return(abcd-ac-bd)


print(karasuba(3841,24165))
