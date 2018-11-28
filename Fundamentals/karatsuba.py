def basicMultiplication(a,b):
    # multiply the larger number by the smaller number

    # cast into list to make life hard
    int1 = [int(i) for i in str(max(a,b))]
    int2 = [int(i) for i in str(min(a,b))]
    partials = []
    # for each digit in smaller number
    for i in int2[::-1]:
        # compute a partial product and store it
        partial = []
        carry = 0
        for j in int1[::-1]:
            partial.insert(0,(carry + (i*j)) % 10)
            carry = ((i*j) + carry)// 10
        if carry != 0:
            partial.insert(0,carry)
        partials.append(partial)
    # add all partial products
    res = 0
    return(partials)

print(basicMultiplication(9,2))
print(basicMultiplication(3841,24165))
