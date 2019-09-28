def sparseSearch(word, list):
    return(doSparseSearch(word,list,0,len(list)))

def doSparseSearch(word, list, start, end):
    mid = start + (end-start)//2
    if list[mid] == "":
        # find closest non-empty
        leftSearch = mid-1
        rightSearch = mid+1
        while True:
            if list[leftSearch] != "":
                mid = leftSearch
                break
            elif list[rightSearch] != "":
                mid = rightSearch
                break
            else:
                leftSearch -= 1
                rightSearch += 1
    if list[mid] == word:
        return(mid)
    elif list[mid] < word:
        return(doSparseSearch(word, list, mid+1, end))
    else:
        return(doSparseSearch(word, list, start, mid))

if __name__=="__main__":
    tInput = (("at",["at", "ball", "", "","car","","","dad","","ring"]),("ring",["at", "ball", "", "car","","","dad","","ring"]),("ball",["at", "ball", "", "","car","",""]),("cat",["at", "", "cat", "","car"]),("dog",["at", "dog", "", "","car"]),("bat",["at", "", "", "bat","car"]))
    tOutput = (0,8,1,2,1,3)
    for i,t in enumerate(tInput):
        print("testing: ", t)
        x = sparseSearch(t[0],t[1])
        print("output: ", x)
        if x != tOutput[i]:
            print("Error: expected ", tOutput[i])
