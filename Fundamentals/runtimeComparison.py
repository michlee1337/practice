import time
import matplotlib.pyplot as plt
import random

def selection_time(arr):
	start = time.time()
	comps = 0

	for i in range(len(arr[1:])):
		min = i
		for j in range(i+1, len(arr)):
			comps += 1
			if arr[j] < arr[min]:
				min = j
		arr[i],arr[min] = arr[min], arr[i]
	end = time.time()
	return([arr,end-start,comps])

def insertion_time(arr):
	start = time.time()
	comps = 0

	for i in range(1,len(arr)):
		for j in range(0,i):
			comps += 1
			if arr[j] > arr[i]:
				arr.insert(j,arr.pop(i))
				break
	end = time.time()
	return([arr,end-start,comps])

def bubble_time(arr):
	start = time.time()
	comps = 0

	for i in range(len(arr)-1,0,-1):
		for j in range(0,i,1):
			comps += 1
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
	end = time.time()
	return([arr,end-start,comps])

def merge_time(arr,comps=0):
	x = len(arr)
	# base casase len arr == 1
	if x == 1:
		return(arr,comps)
	else:
		ret_arr = []

		# recursively sort left and right halves
		l_arr,comp_l = merge_time(arr[:int(x/2)],comps)
		r_arr,comp_r = merge_time(arr[int(x/2):],comps)

		comps = comps + comp_l + comp_r
		l_i = 0
		r_i = 0

		# while there are items in both, compare and append smaller
		while (l_i < len(l_arr)) and (r_i < len(r_arr)):
			comps += 1
			if l_arr[l_i] < r_arr[r_i]:
				ret_arr.append(l_arr[l_i])
				l_i += 1
			else:
				ret_arr.append(r_arr[r_i])
				r_i += 1

		# if anything remaining, append
		while l_i < len(l_arr):
			ret_arr.append(l_arr[l_i])
			l_i += 1

		while r_i < len(r_arr):
			ret_arr.append(r_arr[r_i])
			r_i += 1

		return(ret_arr,comps)


#def testSortAcc(func):

def randList(num,min,max):
	list = []
	for num in range(num+1):
		list.append(int(random.randint(min,max)))
	return(list)

def testLists(num,min,max):
	testL = []
	for i in range(num+1):
		testL.append(randList(i,min,max))
	return(testL)

if __name__ == "__main__":

	# number of lists to test
	n = 10000
	step_size = 1000

	# create list of lists from len 1 to 100
	testL = []
	for i in range(0,n,step_size):
		testL.append(randList(i,-100,100))

	# for each list, run the test and store the number of steps
	#ins_time = [0]*int(n/step_size)
	#sel_time = [0]*int(n/step_size)
	#bubb_time = [0]*int(n/step_size)
	ins_steps = [0]*int(n/step_size)
	sel_steps = [0]*int(n/step_size)
	bubb_steps = [0]*int(n/step_size)
	merge_steps = [0]*int(n/step_size)

	for l in range(len(testL)):
		print('\\')
		_, _,ins_steps[l] = insertion_time(testL[l])
		print('|')
		_, _,sel_steps[l] = selection_time(testL[l])
		print('/')
		_, _,bubb_steps[l] = bubble_time(testL[l])
		print('-')
		_,merge_steps[l] = merge_time(testL[l])
	print('done!')
	print(ins_steps)
	print(sel_steps)
	print(bubb_steps)
	print(merge_steps)

	# plot the time and steps for each sort

	'''
	plt.figure(1)
	plt.subplot(211)
	plt.plot(range(0,n,step_size),ins_time,color="green",label="insertion")
	plt.plot(range(0,n,step_size),sel_time,color="red",label="selection")
	plt.plot(range(0,n,step_size),bubb_time,color="blue",label="bubble")
	plt.legend()


	plt.subplot(212)
	'''
	plt.plot(range(0,n,step_size),ins_steps,color="green",label="insertion")
	plt.plot(range(0,n,step_size),sel_steps,color="red",label="selection")
	plt.plot(range(0,n,step_size),bubb_steps,color="blue",label="bubble")
	plt.plot(range(0,n,step_size),merge_steps,color="yellow",label="merge")
	plt.legend()
	plt.show()
