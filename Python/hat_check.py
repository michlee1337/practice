#____Hat Check____

import random

# generate n hats
def collect_hats(num):
	return([i for i in range(num)])

# return hats at random
def return_hats(arr_hats):
	# store order of returned hats
	return_order = []

	# initialize number of hats
	n = len(arr_hats) - 1

	# while there are still hats
	while len(arr_hats) > 0:
 		# take random hat from storage
		selected_hat = arr_hats.pop(random.randint(0, n))
		n -= 1

		# return hat
		return_order.append(selected_hat)

	# return order of returned hats
	return(return_order)

# check how many hats were returned right
def right_hat(arr_hats):
	i = 0 # initialize index
	tally_right = 0 # initialize return var

	# for each hat
	for hat in arr_hats:
		# if the hat number matches the index
		if hat == i:
			# it was returned right
			tally_right += 1
		i += 1 # increase index
	return(tally_right)

import unittest

class TestHeap(unittest.TestCase):

	def test_collect_hats(self):
		self.assertEqual(collect_hats(3),[0,1,2])
		self.assertEqual(collect_hats(15),[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14])
		self.assertEqual(collect_hats(0),[])

	def test_return_hats(self):
		self.assertTrue(len(return_hats(collect_hats(10)))==10)
		self.assertTrue(len(return_hats(collect_hats(0)))==0)
		self.assertEqual(sorted(return_hats(collect_hats(50))),[i for i in range(50)])

	def test_right_hat(self):
		self.assertEqual(right_hat([0,1,2]),3)
		self.assertEqual(right_hat([0,2,1]),1)
		self.assertEqual(right_hat([0,1,2,4,3,5]),4)
		self.assertEqual(right_hat([]),0)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestHeap)
	unittest.TextTestRunner(verbosity=2).run(suite)



