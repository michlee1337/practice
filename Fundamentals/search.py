def binSearch(arr, x):
	if len(arr) == 0:
		print('not found')
		return('not found')
	i = len(arr)//2
	if arr[i] == x:
		print('found', arr[i])
		return(arr[i])
	elif arr[i] > x:
		binSearch(arr[:i],x)
	else:
		binSearch(arr[i+1:],x)

if __name__ == "__main__":
	print(binSearch([1,2,3,4,5],-5))