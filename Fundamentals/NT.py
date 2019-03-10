#____QUICKSORT____

import random
import unittest

def qsort(lst):
    # start with entire array as segment
    indices = [(0, len(lst))]

    # while there are still segments to consider
    while indices:

        # if segment is one item, end loop
        (frm, to) = indices.pop()
        if frm == to:
            continue

        # if the segment is under 10 items, switch to insertion sort
        if to-frm <= 10:
            # for each elem
            for i in range(frm, to):
                # compare to all elems before it
                for j in range(frm,i):
                    # insert it in right position
                    if lst[j] > lst[i]:
                        lst.insert(j,lst.pop(i))
        
        # else use qsort
        else:
            # get random partition:
            partition = lst[random.randint(frm,to-1)]

            # split into lists:
            lower = [a for a in lst[frm:to] if a < partition]
            upper = [a for a in lst[frm:to] if a > partition]
            counts = sum([1 for a in lst[frm:to] if a == partition]) 

            ind1 = frm + len(lower)
            ind2 = ind1 + counts

            # Put lists into correct place:
            lst[frm:ind1] = lower
            lst[ind1:ind2] = [partition] * counts
            lst[ind2:to] = upper

            # Enqueue other segments to sort
            indices.append((frm, ind1))
            indices.append((ind2, to))
    return lst

#____TESTING____
class TestHeap(unittest.TestCase):

    def test_qsort_on_randomList(self):
        for i in range(10000):
            randL = [random.randint(-100,100) for _ in range(100)]
            self.assertEqual(sorted(randL),qsort(randL))

    def test_qsort_on_edgecases(self):
        repeatedL = [3 for _ in range(50)]
        ascendingL = [val for val in range(50)]
        descendingL = [val for val in range(50,0,-1)]
        zigzagL= [-2,3,0,2,-1,1]
        self.assertEqual([],qsort([]))
        self.assertEqual([1],qsort([1]))
        self.assertEqual(repeatedL, qsort(repeatedL))
        self.assertEqual(ascendingL, qsort(ascendingL))
        self.assertEqual(sorted(descendingL), qsort(descendingL))

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestHeap)
    unittest.TextTestRunner(verbosity=2).run(suite)
