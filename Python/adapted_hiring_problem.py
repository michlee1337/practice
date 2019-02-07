import random
import numpy as np
# __ 10% HIRING __
# simulate hiring period in which the return is a bool list of hire or no on each day
# to be used for more analysis
def sim_hire(days):
	asst = -1 # store current assistant
	hired_arr = [] # record of interview results
	# for each day 
	for i in range(days):
		# interview candidate i
		cand = random.random()
		# if better than current, hire
		if cand > asst:
			asst = cand
			hired_arr.append(1)
			if asst * 1.1 > 1:
				break
		else:
			hired_arr.append(0)
	return(hired_arr)

# avg number of steps it takes to exit sim
def steps_to_end(reps):
	arr_of_steps = []
	for i in range(reps):
		arr_of_steps.append(len(sim_hire(10000)))
	return(np.mean(arr_of_steps))

# avg likelihood of hiring candidate i
def hiring_chances(cand_num,reps):
	i_hire_hist = []
	for i in range(reps):
		sim_res = sim_hire(cand_num)
		if len(sim_res) < cand_num:
			i_hire_hist.append(0)
		else:
			i_hire_hist.append(sim_res[-1])
	return(np.mean(i_hire_hist))




if __name__ == '__main__':
	print(steps_to_end(10000))
	# ~11, avg over 10,000
	print(hiring_chances(2,10000))
	# ~0.5, avg over 10,000
