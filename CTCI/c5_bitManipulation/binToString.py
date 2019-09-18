def binToString(num):
    ret = ""

    for _ in range(32):
        if num == 0:
            print(ret)
            return(0)
        else:
            ret = str(num % 2) + ret
            num = num// 2
    print("ERROR")
    return(1)

if __name__=="__main__":
    binToString(9)
    binToString(99999999)
    binToString(9999999999999999)
