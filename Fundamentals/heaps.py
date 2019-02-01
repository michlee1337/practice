def max_heapify(arr,I):

	# add I to the btottom of the heap
	i = len(arr)
	arr.append(I)

	# while not at root
	while i >= 1:
		# if I is more than parent, swap positions and update i
		if arr[i] > arr[(i-1)//2]:
			arr[i],arr[(i-1)//2] = arr[(i-1)//2],arr[i]
			i = (i-1)//2
		# else, done
		else:
			break
	return(arr)

def build_max_heap(arr):
	# for each item in array, bubble up (max heapify)
	for i in range(1,len(arr),1):
		arr[:i+1] = max_heapify(arr[:i],arr[i])
	return(arr)


if __name__ == "__main__":
	print(max_heapify([],7))
	print(max_heapify([10,5,3,4,1],7))
	print(max_heapify([10,5,3,4,-9],15))
	print(build_max_heap([6,3,-9,1,20,-49]))
	print(build_max_heap([]))
	print(build_max_heap([9,2,6,0,1,4,1]))



