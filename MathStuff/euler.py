# helper funcs

# the rate of change of money in the back < question specific
def roc_money(point):
    return((0.01*point[1])+(250*point[0]))

# formula to find next point using euler method
def find_next(curr_point, step_size, roc_func):
    curr_point[1] = (roc_func(curr_point)*step_size) +curr_point[1]
    curr_point[0] = curr_point[0] + step_size
    return(curr_point)

# main func
def euler_method(curr_point, step_size, roc_func, end_point, path):
    if curr_point[0] >= end_point:
        path.append([curr_point[0],curr_point[1]])
        print(curr_point)
        print(str(path).replace('[',"{").replace(']','}'))
        return(0)
    else:
        path.append([curr_point[0],curr_point[1]])
        euler_method(find_next(curr_point, step_size,roc_func),step_size,roc_func,end_point, path)

print('step size 6')
euler_method([0,0],6,roc_money, 12, [])
print('step size 1')
euler_method([0,0],1,roc_money,12, [])
print('step size 0.02')
euler_method([0,0],0.02,roc_money,12, [])
print('step size 0.015')
euler_method([0,0],0.015,roc_money,12, [])
print('step size 0.013')
euler_method([0,0],0.013,roc_money,12, [])
# how to plot it nicely in function
