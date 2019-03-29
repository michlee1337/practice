#_randomly shuffle until ordered__
import random
import unittest
import heapq
import bisect
import time
import matplotlib.pyplot as plt

def bad_sort(arr):
	# edge case, empty arr
	if len(arr) == 0:
		return(arr)
	# store correct array
	sorted_a = sorted(arr)
	# store length of array
	n = len(arr)

	# while not correct:
	while arr != sorted_a:
		# for each item in array
		for i in range(n):
			# swap with another random item
			j = random.randint(0,n-1)
			arr[i],arr[j] = arr[j],arr[i]
	return(arr)

def approx_median_binSearch(arr,sigma):
	uncertainty = sigma*len(arr)
	running_arr = []
	while len(arr) > 0:
		# add item to running sorted list
		bisect.insort(running_arr,arr.pop(random.randint(0,len(arr)-1)))

		# if odd
		if len(running_arr) % 2 ==1:
			med_ind = len(running_arr)//2

			# if all items checked
			if len(arr) == 0:
				return(running_arr[med_ind])

			# check if we have the range to check with uncertainty
			if uncertainty >= len(arr):
				return(running_arr[med_ind])

		# if even
		else:
			med_ind = [len(running_arr)//2-1,len(running_arr)//2]

			# if all items checked
			if len(arr) == 0:
				return((running_arr[med_ind[0]]+running_arr[med_ind[1]])/float(2))

			# check if we have the range to check with uncertainty
			if uncertainty >= len(arr):
				return((running_arr[med_ind[0]]+running_arr[med_ind[1]])/float(2))


# WIP
def approx_median_heap(arr,sigma):
	min_heap = [arr.pop(0)]
	min_l = 1
	max_heap = [arr.pop(0)]
	max_l = 1
	med = None

	while len(arr) > 0:
		# randomly samply item from arr
		elem = arr.pop(random.randint(0,len(arr)-1))

		# append to shorter heap
		if len(min_heap) > len(max_heap):
			max_heap.insert(0,elem)
			heapq._siftup_max(max_heap,0)
			max_l += 1
		else:
			heapq.heappush(min_heap,elem)
			min_l += 1
		# check if heap elems need to be swapped
		while min_heap[0] < max_heap[0]:
			temp1 = max_heap[0]
			temp2 = min_heap[0]
			heapq._heappushpop_max(max_heap,temp2)
			heapq.heappushpop(min_heap,temp1)

		# calculate median
		if min_l > max_l:
			med = min_l[0]
		elif max_l > min_l:
			med = max_l[0]
		else:
			med = (min_l[0] + max_l[0])/2

		# check if certainly within sigma
		radius = len(arr) # unchecked vars
		# how do i check when heaps aren't fully sorted????
	return(min_heap,max_heap)

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

def getTime(func, reps, *args):
	start = time.time()
	for i in range(reps):
		func(*args)
	end = time.time()
	return((end-start)/reps)

class TestHeap(unittest.TestCase):

	def test_bad_sort(self):
		self.assertEqual(bad_sort([]),[])
		self.assertEqual(bad_sort([4,2,3,5]),[2,3,4,5])
		self.assertEqual(bad_sort([-99,1,43,8,29]),[-99,1,8,29,43])

	def test_approx_median_binSearch(self):
		self.assertTrue((approx_median_binSearch([1,2,3,4,5,6,7,8,9,10],0.5) >= 3) and (approx_median_binSearch([1,2,3,4,5,6,7,8,9,10],0.5) <= 8))
		self.assertTrue((approx_median_binSearch([1,2,3,4,5,6,7,8,9,10],0.25) >= 4) and (approx_median_binSearch([1,2,3,4,5,6,7,8,9,10],0.25) <= 7))
		self.assertTrue((approx_median_binSearch([1,2,3,4,5,6,7,8,9,10],0.15) >= 5) and (approx_median_binSearch([1,2,3,4,5,6,7,8,9,10],0.15) <= 6))

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestHeap)
	unittest.TextTestRunner(verbosity=2).run(suite)


	# number of lists to test
	n = 10000
	step_size = 1000

	# create list of lists from len 1 to 100
	testL = []
	for i in range(0,n,step_size):
		testL.append(randList(i,-100,100))

	# for each list, run the test and store the number of steps
	sigma1 = []
	sigma2 = []
	sigma3 = []
	sigma4 = []
	sigma5 = []
	sigma6 = []

	for l in testL:
		sigma1.append(getTime(approx_median_binSearch,20,l,0.5))
		sigma2.append(getTime(approx_median_binSearch,20,l,0.4))
		sigma3.append(getTime(approx_median_binSearch,20,l,0.3))
		sigma4.append(getTime(approx_median_binSearch,20,l,0.2))
		sigma5.append(getTime(approx_median_binSearch,20,l,0.1))
		sigma6.append(getTime(approx_median_binSearch,20,l,0))

	plt.plot(range(0,n,step_size),sigma1,color="purple",label="sigma 0.5")
	plt.plot(range(0,n,step_size),sigma2,color="blue",label="sigma 0.4")
	plt.plot(range(0,n,step_size),sigma3,color="green",label="sigma 0.3")
	plt.plot(range(0,n,step_size),sigma4,color="red",label="sigma 0.2")
	plt.plot(range(0,n,step_size),sigma5,color="orange",label="sigma 0.1")
	plt.plot(range(0,n,step_size),sigma6,color="yellow",label="sigma 0.0")
	plt.legend()
	plt.show()


