def urlify(c_arr, t_len):
    # O(n) time
    # O(1) space
    j = len(c_arr) - 1 #pointer to track ammended string
    # for each char starting from the end
    for i in range(t_len-1,0,-1):
        if c_arr[i] == " ":
            # add %20 ending at pointer j
            c_arr[j-2:j+1] = ["%","2","0"]
            j -= 3
        else:
            # move char to pointer j
            c_arr[j] = c_arr[i]
            j -= 1
    return(c_arr)

if __name__=="__main__":
    inputArr = list(input("your str: "))
    true_len = int(input("t len: "))
    print(urlify(inputArr,true_len))
