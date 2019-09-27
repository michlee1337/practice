def sparseSearch(word, list):
    return(doSparseSearch(word,list,0,len(list)))

def doSparseSearch(word, list, start, end):
    mid = start + (end-start)//2
    if list[mid] == word:
        return(mid)
    elif list[mid] == "":
        return(max(doSparseSearch(word, list, start, mid),doSparseSearch(word, list, mid+1, end)))
    elif list[mid] < word:
        return(doSparseSearch(word, list, start, mid))
    else:
        return(doSparseSearch(word, list, mid+1, end))
