def magicIndex(inp_arr,start_ind = 0):
    # O(n) time, arguably expected lgn?
    # O(n) space - for each call

    # edge: handle null:
    if len(inp_arr) == 0:
        return([])

    if len(inp_arr) == 1:
        if inp_arr[0] == start_ind:
            return(inp_arr)
        else:
            return([])

    med_ind = len(inp_arr)//2

    if inp_arr[med_ind] == start_ind+med_ind:
        return(magicIndex(inp_arr[0:med_ind],start_ind) + inp_arr[med_ind:med_ind+1] + magicIndex(inp_arr[med_ind+1:],start_ind+med_ind+1))
    elif inp_arr[med_ind] > med_ind:
        return(magicIndex(inp_arr[0:med_ind],start_ind))
    else:
        return(magicIndex(inp_arr[med_ind:],med_ind))

#______ if not distinct

def magicIndexND(inp_arr,start_ind = 0):
    # O(n) time
    # O(n) space - for each call

    # edge: handle null:
    if len(inp_arr) == 0:
        return([])

    if len(inp_arr) == 1:
        if inp_arr[0] == start_ind:
            return(inp_arr)
        else:
            return([])

    med_ind = len(inp_arr)//2

    if inp_arr[med_ind] == start_ind+med_ind:
        return(magicIndex(inp_arr[0:med_ind],start_ind) + inp_arr[med_ind:med_ind+1] + magicIndex(inp_arr[med_ind+1:],start_ind+med_ind+1))
    elif inp_arr[med_ind] > med_ind:
        leftMI = magicIndex(inp_arr[0:med_ind],start_ind)
        if leftMI:
            return(leftMI)
        else:
            rightMI = magicIndex(inp_arr[inp_arr[med_ind]:],start_ind+inp_arr[med_ind])
            return(rightMI)
    else:
        rightMI = magicIndex(inp_arr[med_ind:],med_ind)
        if rightMI:
            return(rightMI)
        else:
            leftMI = magicIndex(inp_arr[:inp_arr[med_ind]],start_ind)
            return(leftMI)

if __name__ == "__main__":
    inp_arr = input("list seperated by spaces: ").split()
    inp_arr = [int(c) for c in inp_arr]
    print(magicIndex(inp_arr))
