def max_heapify(arr,I):

	# add I to the btottom of the heap
	i = len(arr)
	arr.append(I)

	# while not at root
	while i >= 1:
		print(i)
		# if I is more than parent, swap positions and update i
		print('comparing',arr[i],arr[(i-1)//2])
		if arr[i] > arr[(i-1)//2]:
			arr[i],arr[(i-1)//2] = arr[(i-1)//2],arr[i]
			i = (i-1)//2
		# else, done
		else:
			break
	return(arr)


if __name__ == "__main__":
	print(max_heapify([],7))
	print(max_heapify([10,5,3,4,1],7))
	print(max_heapify([10,5,3,4,-9],15))

