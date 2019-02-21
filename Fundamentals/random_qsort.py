import timeit
import random

eps = 1e-16
N = 10000
locations = [0.0, 0.5, 1.0 - eps]


def median(x1, x2, x3):
    if (x1 < x2 < x3) or (x3 < x2 < x1):
        return x2
    elif (x1 < x3 < x2) or (x2 < x3 < x1):
        return x3
    else:
        return x1

def qsort(lst):
    indices = [(0, len(lst))]

    while indices:
        (frm, to) = indices.pop()
        if frm == to:
            continue

        # Find the partition:
        N = to - frm
        inds = [frm + int(N * n) for n in locations]
        values = [lst[ind] for ind in inds]
        partition = median(*values)

        # Split into lists:
        lower = [a for a in lst[frm:to] if a < partition]
        upper = [a for a in lst[frm:to] if a > partition]
        counts = sum([1 for a in lst[frm:to] if a == partition])
        

        ind1 = frm + len(lower)
        ind2 = ind1 + counts

        # Push back into correct place:
        lst[frm:ind1] = lower
        lst[ind1:ind2] = [partition] * counts
        lst[ind2:to] = upper

        # Enqueue other locations
        indices.append((frm, ind1))
        indices.append((ind2, to))
    return lst


def qsort_NE(lst):
    indices = [(0, len(lst))]

    while indices:
        (frm, to) = indices.pop()
        if frm == to:
            continue

        # Find the partition:
        N = to - frm
        inds = [frm + int(N * n) for n in locations]
        values = [lst[ind] for ind in inds]
        partition = median(*values)

        # move partition to front
        part_pos = lst.index(partition)
        if part_pos != 0:
            lst[part_pos],lst[frm] = lst[frm],lst[part_pos]

        # Split into lists:
        lower = [a for a in lst[frm+1:to] if a < partition]
        upper = [a for a in lst[frm+1:to] if a > partition]        

        ind = frm + len(lower)

        # Push back into correct place:
        lst[frm:ind] = lower
        lst[ind] = partition
        lst[ind+1:to] = upper

        # Enqueue other locations
        indices.append((frm, ind))
        indices.append((ind+1, to))
    return lst

def qsort_NM(lst):
    indices = [(0, len(lst))]

    while indices:
        (frm, to) = indices.pop()
        if frm == to:
            continue

        # Find the partition:
        N = to - frm
        partition = lst[frm]

        # Split into lists:
        lower = [a for a in lst[frm:to] if a < partition]
        upper = [a for a in lst[frm:to] if a > partition]
        counts = sum([1 for a in lst[frm:to] if a == partition])
        

        ind1 = frm + len(lower)
        ind2 = ind1 + counts

        # Push back into correct place:
        lst[frm:ind1] = lower
        lst[ind1:ind2] = [partition] * counts
        lst[ind2:to] = upper

        # Enqueue other locations
        indices.append((frm, ind1))
        indices.append((ind2, to))
    return lst

def qsort_recur(lst,frm=0,to=N):
    if frm == to:
        return(lst)

    else:

        # Find the partition:
        N = to - frm
        inds = [frm + int(N * n) for n in locations]
        values = [lst[ind] for ind in inds]
        partition = median(*values)

        # Split into lists:
        lower = [a for a in lst[frm:to] if a < partition]
        upper = [a for a in lst[frm:to] if a > partition]
        counts = sum([1 for a in lst[frm:to] if a == partition])
        

        ind1 = frm + len(lower)
        ind2 = ind1 + counts

        # Push back into correct place:
        lst[frm:ind1] = lower
        lst[ind1:ind2] = [partition] * counts
        lst[ind2:to] = upper

        # Enqueue other locations
        qsort_recur(lst,frm,ind1)
        qsort_recur(lst,ind2,to)
    return lst


def randomized_quicksort():
    lst = [i for i in range(N)]
    random.shuffle(lst)
    return qsort(lst)

def randomized_quicksort_NE():
    lst = [i for i in range(N)]
    random.shuffle(lst)
    return qsort_NE(lst)

def randomized_quicksort_NM():
    lst = [i for i in range(N)]
    random.shuffle(lst)
    return qsort_NM(lst)

def randomized_quicksort_recur():
    lst = [i for i in range(N)]
    random.shuffle(lst)
    return qsort_recur(lst)

def test_quicksort():
    lst = randomized_quicksort()
    assert (lst == [i for i in range(N)])

def test_quicksort_NE():
    lst = randomized_quicksort_NE()
    assert (lst == [i for i in range(N)])

def test_quicksort_NM():
    lst = randomized_quicksort_NM()
    assert (lst == [i for i in range(N)])

def test_quicksort_recur():
    lst = randomized_quicksort_recur()
    assert (lst == [i for i in range(N)])

# Is our algorithm correct
test_quicksort()
test_quicksort_NE()
test_quicksort_NM()
test_quicksort_recur()

# Difference in time without seperating the equal to partition
print('time with equality: ',timeit.timeit(randomized_quicksort, number=1))
print('time w/o equality: ',timeit.timeit(randomized_quicksort_NE, number=1))
print('time w/o median : ',timeit.timeit(randomized_quicksort_NM, number=1))
print('time recur : ',timeit.timeit(randomized_quicksort_recur, number=1))