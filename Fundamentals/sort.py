import time

def insertionSort(arr):
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
def runTime(function, *arg1):
    start = time.time()
    print(function(*arg1))
    end = time.time()
    print('time: ',start-end)


if __name__ == "__main__":
    runTime(insertionSort,[])
    runTime(insertionSort,[0])
    runTime(insertionSort,[23,4,-1,0,399])
