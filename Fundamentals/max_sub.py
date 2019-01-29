def maxSub_brute(arr):

	# running record of max sum and indexes
	max = None
	max_s = []

	# for every possible starting index i
	for i in range(len(arr)):
		sub = 0

		# for every possible ending index after i
		for j in range(len(arr)-i):
			sub += arr[i+j]

			# if current sum larger than recorded, update
			if max is None or sub > max:
				max = sub
				max_s = arr[i:i+j+1]
	return(max_s)

def maxSub_linear(arr):
	# keep track of overall max 
	maxSum_ovr = float('-inf')
	maxArr_ovr = []

	# keep track of max ending in last index
	maxSum_end = 0
	maxArr_end = []

	# for each i in arr
	for i in range(len(arr)):
		# update max ending in last index
		
		# max ending at last index is either:
		# current index (only)
		maxSum_end += arr[i]

		if arr[i] > maxSum_end:
			maxSum_end = arr[i]
			maxArr_end = [arr[i]]

		# or past max + current
		else:
			maxArr_end.append(arr[i])
		
		# if larger than overall max, update
		if maxSum_end > maxSum_ovr:
			maxSum_ovr = maxSum_end
			maxArr_ovr = maxArr_end

	# checking edge case: empty array
	if maxSum_ovr == float('-inf'):
		maxSum_ovr = 0


	return(maxSum_ovr, maxArr_ovr)

def max_addOne(x, mx):
	# find max ending in last index
	# keep track of running max ending in n
	maxSum = float('-inf')
	# keep track of sum up til current index
	sum_curr = 0

	# for each index from last to first
	for i in range(len(x)-1,-1,-1):
		# add new i to sum_Curr
		sum_curr += x[i]

		# if current sum more than global, update
		if sum_curr > maxSum:
			maxSum = sum_curr
	# return larger of old max sum or new max sum
	if mx > maxSum:
		return(mx)
	else:
		return(maxSum)

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


def closeFar(arr):
	if len(arr) < 2:
		return('less than 2 is not a pair :(')
	arr_s = quickSort(arr)
	far = [arr_s[0],arr_s[-1]]
	least_dist = float('inf')
	close = []
	for i in range(1,len(arr_s),1):
		if abs(arr_s[i] - arr_s[i-1]) < least_dist:
			least_dist = arr_s[i] - arr_s[i-1]
			close = [arr_s[i],arr_s[i-1]]
	return(close,far)

	# T(n) approx= nlgn + n (but quicksort worst case n^2)
	# O(n) = n^2
	# omega(n) = nlgn
	# average case = nlgn


if __name__ == "__main__":
	print(maxSub_linear([-1,2,3,-4,5,10]))
	print(maxSub_linear([1,-2,3]))
	print(maxSub_linear([]))
	print(maxSub_linear([-2,-3,-1,-4,-6]))
	print(max_addOne([-1,2,3,-4,5,10],6))
	print(max_addOne([1,-2,3],1))
	print(max_addOne([-2,-3,-1,-4,-6, -1],-1))
	print(closeFar([4,-10,2]))
	print(closeFar([4,-10,2,9999,-89,-90]))


