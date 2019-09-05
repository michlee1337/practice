def isWordSquare(w_list):
    n = len(w_list)
    for i in range(n):
        for j in range(n):
            if w_list[j][i] != w_list[i][j]:
                print(j,i)
                print(w_list[j][i],w_list[i][j])
                return(False)
    return(True)

if __name__=="__main__":
    w_list = input("word list: ").split()
    print(w_list)
    print(isWordSquare(w_list))
