def powerSet(inp_arr):
    # time: O(2^n) - calls itself n times, each call takes 2^iteration time
    # space: O(2^n) - at any one point only holds 2^i items

    # edge case
    if len(inp_arr) == 0:
        return([])

    if len(inp_arr) == 1:
        return([input_arr,[]])

    # inductive step: num set is always []+powerSet(arr-x) + [x]+powerSet(arr-x)
    else:
        ss_wo = powerSet(inp_arr[1:])
        ss_w = [ss.append(inp_arr[0]) for ss in ss_wo]
        return(ss_wo + ss_w)
