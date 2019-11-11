def _m_dist(worker,bike):
    return(abs(bike[1]-worker[1]) + abs(bike[0]-worker[0]))


def campusBikes(workers,bikes):
    '''
    backtracking: O(N!)
    for each worker
        - try assigning a bike, assigning the rest and check sum
        - take min

    optimize: memo/ dict
    '''
    # edge case
    if len(workers) == 0:
        return(0)

    m_dict = [[None] * len(bikes) for _ in range(len(workers))]

    # build memo
    # m_dict[w_ind][b_ind] = distance between w and bike
    for w_ind, worker in enumerate(workers):
        for b_ind, bike in enumerate(bikes):
            m_dict[w_ind][b_ind] = _m_dist(worker, bike)

    return(campusBikesDp(workers, bikes, 0, 0, m_dict))

def campusBikesDp(workers, bikes, w_ind, m_dict):
    print("assigning",w_ind)
    # base case
    if len(bikes) == b_ind:
        return(0)

    min_sum = float('inf')
    for ind, bike in enumerate(bikes[b_ind:]):
        possible_assignment = m_dict[w_ind][ind] + campusBikesDp(workers, bikes, w_ind+1, b_ind+1, m_dict)
        print(possible_assignment, w_ind,ind)
        if possible_assignment < min_sum:
            min_sum = possible_assignment

    return(min_sum)
print(campusBikes([[0,0],[2,1]], [[1,2],[3,3]])) #6
print(campusBikes([[0,0],[1,1],[2,0]],[[1,0],[2,2],[2,1]])) #4
