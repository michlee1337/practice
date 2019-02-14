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

def fib(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    
#__MAIN__

import random
random.seed(123)
lst1 = [random.random() for a in range(100)]
lst2 = range(100)

import time
    

start = time.time()
quickSort(lst1)
end = time.time()
print(end-start)

start = time.time()
quickSort(lst2)
end = time.time()
print((end-start))

# i bumped down the list sizes because my comp 
# is reaching max recursion depth

start = time.time()
fib(100)
end = time.time()
print(end-start)
