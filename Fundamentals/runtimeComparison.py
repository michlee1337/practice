import time
import matplotlib.pyplot as plt
import random

def selection_time(arr):
	start = time.time()
	steps = 0

	for i in range(len(arr[1:])):
		min = i
		steps += 1
		for j in range(i+1, len(arr)):
			steps += 1
			if arr[j] < arr[min]:
				min = j
				steps += 1
		arr[i],arr[min] = arr[min], arr[i]
		steps += 3
	end = time.time()
	return([arr,end-start,steps])

def insertion_time(arr):
	start = time.time()
	steps = 0

	for i in range(1,len(arr)):
		for j in range(0,i):
			steps += 1
			if arr[j] > arr[i]:
				arr.insert(j,arr.pop(i))
				steps += 2 + len(arr)-j
				break
	end = time.time()
	return([arr,end-start,steps])

def bubble_time(arr):
	start = time.time()
	steps = 0

	for i in range(len(arr)-1,0,-1):
		for j in range(0,i,1):
			steps += 1
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				steps += 3
	end = time.time()
	return([arr,end-start,steps])

def merge_time(arr,comps=0):
	x = len(arr)
	# base casase len arr == 1
	if x == 1:
		return(arr,comps)
	else:
		ret_arr = []

		# recursively sort left and right halves
		l_arr,_ = merge_time(arr[:int(x/2)],comps)
		r_arr,_ = merge_time(arr[int(x/2):],comps)

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
	print(merge_time([-99,1,2,4,0,3,3,2,1]))
	'''
	# number of lists to test
	n = 10000
	step_size = 1000

	# create list of lists from len 1 to 100
	testL = []
	for i in range(0,n,step_size):
		testL.append(randList(i,-100,100))

	# for each list, run the test and store the number of steps
	ins_time = [0]*int(n/step_size)
	sel_time = [0]*int(n/step_size)
	bubb_time = [0]*int(n/step_size)
	ins_steps = [0]*int(n/step_size)
	sel_steps = [0]*int(n/step_size)
	bubb_steps = [0]*int(n/step_size)

	for l in range(len(testL)):
		print('\\')
		_, ins_time[l],ins_steps[l] = insertion_time(testL[l])
		print('|')
		_, sel_time[l],sel_steps[l] = selection_time(testL[l])
		print('/')
		_, bubb_time[l],bubb_steps[l] = bubble_time(testL[l])
		print('-')
	print('done!')

	# plot the time and steps for each sort

	plt.figure(1)
	plt.subplot(211)
	plt.plot(range(0,n,step_size),ins_time,color="green",label="insertion")
	plt.plot(range(0,n,step_size),sel_time,color="red",label="selection")
	plt.plot(range(0,n,step_size),bubb_time,color="blue",label="bubble")
	plt.legend()

	plt.subplot(212)
	plt.plot(range(0,n,step_size),ins_steps,color="green",label="insertion")
	plt.plot(range(0,n,step_size),sel_steps,color="red",label="selection")
	plt.plot(range(0,n,step_size),bubb_steps,color="blue",label="bubble")
	plt.legend()
	plt.show()

	'''