def insert(N,M,i,j):
    n = len(bin(N))

    clearN = (0xff << (j + 1)) | ((1<<i) - 1)

    insertM = M<<i

    return((N & clearN) | insertM)


    #clearN = int('1'*(n-j-1)+'0'*(j-i+1)+'1'*(i),2)
    # add M to N
    #addM = int('0'*(n-j-1)+str(M)+'0'*(i),2)

    #print(bin((N & clearN)|addM))


if __name__=="__main__":
    print(bin(insert(0b10000000000,0b10011,2,6)))
