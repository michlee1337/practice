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
	maxInd_ovr = []

	# keep track of max ending in last index
	maxSum_end = 0
	maxInd_end = []

	# for each i in arr
	for i in range(len(arr)):
		# update max ending in last index
		
		# max ending at last index is either:
		# current index (only)
		maxSum_end += arr[i]

		if arr[i] > maxSum_end:
			maxSum_end = arr[i]
			maxInd_end = [arr[i]]

		# or past max + current
		else:
			maxInd_end.append(arr[i])
		
		# if larger than overall max, update
		if maxSum_end > maxSum_ovr:
			maxSum_ovr = maxSum_end
			maxInd_ovr = maxInd_end

	# checking edge case: empty array
	if maxSum_ovr == float('-inf'):
		maxSum_ovr = 0


	return(maxSum_ovr, maxInd_ovr)


if __name__ == "__main__":
	print(maxSub_linear([-1,2,3,-4,5,10]))
	print(maxSub_linear([1,-2,3]))
	print(maxSub_linear([]))
	print(maxSub_linear([-2,-3,-1,-4,-6]))


