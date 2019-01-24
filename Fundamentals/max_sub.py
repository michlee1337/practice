def maxSub_brute(arr):
	max = None
	max_s = []
	for i in range(len(arr)):
		sub = 0
		for j in range(len(arr)-i):
			sub += arr[i+j]
			if max is None or sub > max:
				max = sub
				max_s = arr[i:i+j+1]
				print(max, max_s)
	return(max_s)

if __name__ == "__main__":
	print(maxSub_brute([1,-2,3]))