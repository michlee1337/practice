# quicksort

def quickSort(arr):
	# select pivot
	pivot = arr[-1]
	j = len(arr-1)

	# put pivot in right order
	i = 0
	while arr[i] < pivot:
		i += 1
	arr[j],arr[i] = arr[i],arr[j]

	# recurse on branches
	quickSort(arr[0,i])
	quickSort(arr[i+1,-1])