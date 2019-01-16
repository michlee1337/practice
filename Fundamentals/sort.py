def insertionSort(arr):
    for i in range(len(arr[1:])):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i],arr[min] = arr[min], arr[i]
    return(arr)

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


if __name__ == "__main__":
    print(insertionSort([]))
    print(insertionSort([0]))
    print(insertionSort([23,4,-1,0,399]))
    #print(mergeSort([19,47,2792,3,4,2]))
