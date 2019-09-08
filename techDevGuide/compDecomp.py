import sys

def decomp(c_str):
    return(doDecomp(c_str,0))

def doDecomp(c_str, p):
    str = ""
    rep = 0

    # while still processing
    while len(c_str) > p:
        # digit: update str and pointer
        if c_str[p].isdigit():
            endp = p
            while c_str[endp].isdigit():
                endp += 1
            rep = int(c_str[p:endp])
            subStr, p = doDecomp(c_str, endp+1) # +1 to skip the open bracket
            str += rep * subStr
        # close bracket: return
        elif c_str[p] == "]":
            return(str, p+1)
        # char: just add
        else:
            str += c_str[p]
            p += 1
    return(str)

if __name__=="__main__":
    print(decomp(sys.argv[1]))
