#___________RECURSIVE_______________

def cut_rod(prices,n):
    # base case
    if n==0:
        return 0
    
    # recuse
    q = -float("inf")
    for i in range(n):
        # return max of price of a cut + max price of subrod
        q = max(q,prices[i]+cut_rod(prices,n-i-1))
    return(q)

#___________DYNAMIC_______________
def extended_bottom_up_cut_rod(prices,n):
    r = [0] * (n+1)
    s = [0] * (n+1)
    for i in range(1,1+n):
        q = -float("inf")
        for j in range(1,1+i):
            # store max price + optimum cut
            if q < prices[j-1] + r[i-j]:
                q = prices[j-1] + r[i-j]
                s[i] = j
        r[i] = q
    return(r,s)

def print_cut_rod_solution(prices,n):
    r,s = extended_bottom_up_cut_rod(prices,n)
    while n>0:
        print(s[n])
        n = n-s[n]

#___________TEST__________________
assert(cut_rod([1,2,3,4,7],5) == 7)
assert(cut_rod([1,8,7,4,5],5) == 17)
assert(extended_bottom_up_cut_rod([2,2,3,4,13],5) == ([0, 2, 4, 6, 8, 13], [0, 1, 1, 1, 1, 5]))
assert(extended_bottom_up_cut_rod([1,8,7,4,5],5)==([0, 1, 8, 9, 16, 17], [0, 1, 2, 1, 2, 1]))
print_cut_rod_solution([1,8,7,4,5],5)
print(':)')

#______________TIME and PLOT_________

import time
import random

def getTime(func, reps, *args):
	start = time.time()
	for i in range(reps):
		func(*args)
	end = time.time()
	return((end-start)/reps)

r_time = []
d_time = []
for i in range(20):
    price = [random.randint(0,i) for _ in range(i)]
    r_time.append(getTime(cut_rod,10,price,i))
    d_time.append(getTime(extended_bottom_up_cut_rod,10,price,i))


import matplotlib.pyplot as plt

plt.plot(r_time,label="recursive",color="red")
plt.plot(d_time,label="dynamic",color="blue")
plt.title("Performance on Rod Cutting Problem")
plt.legend()
plt.show()

