#_______Heaps________

# helper functions
def leftChild(i):
	return(i*2+1)

def rightChild(i):
	return(i*2+2)

def parent(i):
	return((i-1)//2)

# private func, sift down

def _sift_down(A,pos):
	# from position to leaf
	print('called')
	for i in range(pos,len(A)//2,1):
	# find largest between i and children
		if A[i] >= A[leftChild(i)]:
			if A[i] >= A[rightChild(i)]:
				# i in right position, break out.
				break
			else: 
				#right largest, swap with i
				A[i], A[rightChild(i)] = A[rightChild(i)], A[i]
		elif A[leftChild(i)] >= A[rightChild(i)]:
			# left largest, swap with i
			A[i], A[leftChild(i)] = A[leftChild(i)], A[i]
		else:
			# right largest, swap with i
			A[i], A[rightChild(i)] = A[rightChild(i)], A[i]
	return(A)


# max heapify, essentially sift "up" (parent to child)

def max_heapify(A,i):
	max_ind = len(A) - 1
	# find largest between i and children
	if leftChild(i) > max_ind or A[i] >= A[leftChild(i)]:
		if rightChild (i) > max_ind or A[i] >= A[rightChild(i)]:
			# i largest, don't change
			pass
		else: 
			#right largest, swap with i
			A[i], A[rightChild(i)] = A[rightChild(i)], A[i]
			# recurse on new index of focus node
			max_heapify(A,rightChild(i))
	elif rightChild (i) > max_ind or A[leftChild(i)] >= A[rightChild(i)]:
		# left largest, swap with i
		A[i], A[leftChild(i)] = A[leftChild(i)], A[i]
		# recurse on new index of focus node
		max_heapify(A,leftChild(i))
	else:
		# right largest, swap with i
		A[i], A[rightChild(i)] = A[rightChild(i)], A[i]
		# recurse on new index of focus node
		max_heapify(A,rightChild(i))
	return(A)

# build max heap

def build_max_heap(A):
	# for each node in heap
	# from last non-leaf node
	# to root
	for i in range(len(A)//2 -1, -1, -1):
		# ensure the node + children are a max heap
		max_heapify(A,i)
	return(A)

# heappush: add item to heap

def heappush(A, I):
	# add I to the btottom of the heap
	i = len(A)
	A.append(I)

	# while not at root
	while i >= 1:
		# if I is more than parent, swap positions and update i
		if A[i] > A[(i-1)//2]:
			A[i],A[(i-1)//2] = A[(i-1)//2],A[i]
			i = (i-1)//2
		# else, done
		else:
			break
	return(A)

# heappop: pop and return root item

def heappop(A):
	if len(A) == 0:
		return('error! empty arr')
	# store root item
	ret = A[0]
	# replace root with last item
	A[0] = A.pop()
	# bubble root down into correct position
	_sift_down(A,0)
	return(ret,A)

import unittest

class TestHeap(unittest.TestCase):

	def test_max_heapify(self):
		self.assertEqual(max_heapify([4,2,3,5],1),[4,5,3,2])
		self.assertEqual(max_heapify([4,5,2,3],0),[5,4,2,3])

	def test_build_max_heap(self):
		self.assertEqual(build_max_heap([6,3,-9,1,20,-49]),[20,6,-9,1,3,-49])
		self.assertEqual(build_max_heap([]),[])
		self.assertEqual(build_max_heap([9,2,6,0,1,4,1]),[9,2,6,0,1,4,1])

	def test_heappush(self):
		self.assertEqual(heappush([5,4,2,3],7),[7,5,2,3,4])
		self.assertEqual(heappush([],7),[7])
		self.assertEqual(heappush([15,14,13],7),[15,14,13,7])

	def test_heappop(self):
		self.assertEqual(heappop([5,4,2,3]),(5,[4,3,2]))
		self.assertEqual(heappop([]),'error! empty arr')

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestHeap)
	unittest.TextTestRunner(verbosity=2).run(suite)

