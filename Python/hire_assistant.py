#____Hire Assistant Problem____
import random
import numpy as np
import matplotlib.pyplot as plt
import math

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

# main code

# set params
min_period = 1
max_period = 10000
step_size = 100
avg_over = 30

# simulate and store results
sim_results = []
for i in range(avg_over):
	sim_results.append(sim_hiring_periods(min_period,max_period, step_size))

# average results
avg_res = np.mean(sim_results,axis=0)

# calculate theoretical
x = range(min_period,max_period+1,step_size)
y = [math.log(i) + 1 for i in x]

# plot real
plt.plot(x,avg_res,label="real")
# plot theoretical
plt.plot(x,y,label="theoretical")
plt.xlabel('Length of Hiring Period (days)')
plt.ylabel('Avg Hires (over'+str(avg_over)+')')
plt.title('Avg Hires over Length of Hiring Period')
plt.legend()
plt.show()


import unittest

class TestHeap(unittest.TestCase):

	def test_sim_hiring_days(self):
		self.assertTrue(sim_hiring_days(10) >= 0 and sim_hiring_days(10) <= 10)
		self.assertTrue(sim_hiring_days(3) >= 0 and sim_hiring_days(3) <= 3)
		self.assertEqual(sim_hiring_days(0),0)

	def test_sim_hiring_periods(self):
		self.assertEqual(len(sim_hiring_periods(1,10,1)),10)
		self.assertEqual(len(sim_hiring_periods(1,15,5)),3)
		self.assertTrue(sim_hiring_periods(1,10,1)[9]<=10)
		self.assertTrue(sim_hiring_periods(1,15,5)[2]<=15)

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestHeap)
	unittest.TextTestRunner(verbosity=2).run(suite)



