import time

def insertion_time(arr):
	start = time.time()
	steps = 0

	for i in range(len(arr[1:])):
		min = i
		steps += 1
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min]:
				min = j
				steps += 1
		arr[i],arr[min] = arr[min], arr[i]
		steps += 3
	end = time.time()
	print('time: ', start-end)
	print('steps: ', steps)
	print('solution: ',arr)
	return(arr)




if __name__ == "__main__":
	insertion_time([])
	insertion_time([0])
	insertion_time([99,-33,-2,4,3,59])