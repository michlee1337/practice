# quicksort

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

if __name__ == "__main__":
	print(quickSort([2,1,3]))
	print(quickSort([99,0,-14,2,1,3]))
	print(quickSort([-99,0,-14,-2,-8,3]))
	print(quickSort([]))
	print(quickSort([3]))
	print(quickSort([3,3,3,3,3]))