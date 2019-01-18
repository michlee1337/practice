import time

def SelectionSort(arr):
    for i in range(len(arr[1:])):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min], arr[i]
    return(arr)


def quickSort(arr):
    if len(arr) <= 1:
        return(arr)

    # select last elem as pivot
    j = len(arr)-1

    # sort arr so all items less than pivot are on left of the rest
    i = 0
    k = j-1

    while i <= k:
        while i <= j and arr[i] <= arr[j]:
            i += 1
        while k >= 0  and arr[k] >= arr[j]:
            k -= 1
        if i < k:
            arr[k],arr[i] = arr[i],arr[k]

    # recurse on items less than and more than pivot
    return(quickSort(arr[0:k+1]) + [arr[j]] + quickSort(arr[k+1:-1]))


def mergeSort(arr):
    if len(arr) == 1:
        return(arr)
    else:
        # divide
        mid = len(arr)//2
        left_sorted = mergeSort(arr[:mid])
        right_sorted = mergeSort(arr[mid:])

        sorted = []

        # conquer
        while len(left_sorted) > 0 and len(right_sorted) > 0:
            if left_sorted[0] < right_sorted[0]:
                sorted.append(left_sorted.pop(0))
            else:
                sorted.append(right_sorted.pop(0))

        for i in range(len(left_sorted)):
            sorted.append(left_sorted.pop(0))

        for i in range(len(right_sorted)):
            sorted.append(right_sorted.pop(0))

        return(sorted)

def runTime(function, *args):
    start = time.time()
    print(function(*args))
    end = time.time()
    print('time: ',start-end)

def recursive_ins(arr,n):
    # base case: arr len 1
    if n <= 0:
        return(arr,n+1)

    else:
        # sort list except last
        n_arr,n = recursive_ins(arr[0:n],n-1)

        # add last back
        n_arr = n_arr + [arr[n]]

        # sort last into arr
        for j in range(n-1,-1,-1):
            if j == 0 or n_arr[n] >= n_arr[j]:
                n_arr.insert(j,n_arr.pop(n))
                return(n_arr,n+1)


if __name__ == "__main__":
    #runTime(SelectionSort,[])
    #runTime(SelectionSort,[0])
    #runTime(SelectionSort,[23,4,-1,0,399])
    #print(recursive_ins([3,2,1,1,2,3,1],6))
    #print(recursive_ins([3,2,1],2))
    print(recursive_ins([3,2,-11],2))
    print(recursive_ins([],-1))
    print(recursive_ins([1],0))


