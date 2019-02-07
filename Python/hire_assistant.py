#____Hire Assistant Problem____
import random

# simulate one hiring period
def sim_hiring_days(days):
	asst = -1 # store current assistant
	num_hired = 0 # store num of asst hired
	# for each day 
	for i in range(days):
		# interview candidate i
		cand = random.random()
		# if better than current, hire
		if cand > asst:
			asst = cand
			num_hired += 1
	return(num_hired)

# simulate over multiple hiring periods
def sim_hiring_periods(start,stop, step):
	num_hired = []
	# for each period length specified
	for i in range(start, stop+1,step):
		# run simulation for that period length
		# store the number of hires within the period
		num_hired.append(sim_hiring_days(i))
	return(num_hired)

# average result



import unittest

class TestHeap(unittest.TestCase):

	def test_sim_hiring_days(self):
		self.assertTrue(sim_hiring_days(10) >= 0 and sim_hiring_days(10) <= 10)
		self.assertTrue(sim_hiring_days(3) >= 0 and sim_hiring_days(10) <= 3)
		self.assertEqual(sim_hiring_days(0),0)

	def test_sim_hiring_periods(self):
		self.assertTrue(len(sim_hiring_periods(1,10,1))==10)
		self.assertTrue(len(sim_hiring_periods(1,15,5))==3)
		self.assertTrue(sim_hiring_periods(1,10,1)[9]<=10)
		self.assertTrue(sim_hiring_periods(1,15,5)[2]<=15)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestHeap)
	unittest.TextTestRunner(verbosity=2).run(suite)