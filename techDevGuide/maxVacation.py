import sys
import ast

class Solution:
    maxDays = 0

    def maxVacation(self, flights, days):
        '''
        Inputs:
            flights: {2d array} flight[i][j] indicates if there is a flight from city i to city j
            days: {2d array} days[i][j] indicates how many vacation days can be taken in city i on week j+1
        Output:
            Maximum # of vacation days possible
        Constraints:
            Can only fly once a week (on Monday, first day of the week)
        '''

        # brute force: try every possible permutation, that's O(n!) time
        return(self._findMaxVacation(flights, days, 0, 0, 0))

    def _findMaxVacation(self, flights, days, city, week, curDays):
        # base case: if week = last week, end and remember the max value of this path
        if week == len(days[0]):
            Solution.maxDays = max(curDays, Solution.maxDays)
            return(0)
        # recursive step: try all possible path
        else:
            for i,_ in enumerate(flights):
                if (i == city or flights[city][i]):
                    self._findMaxVacation(flights, days, i, week + 1, curDays + days[i][week])

        # dp

        # approach: bottom up dp
        # what matters is _what city you're in_ + _what week_
        # 2d memoization of ^^

        # best is best of best(any city, last week) + best(any reachable city from last week, this week) and best(this week, this city)

if __name__=="__main__":
    flights = ast.literal_eval(sys.argv[1])
    days = ast.literal_eval(sys.argv[2])
    print("flights: ", flights)
    print("days: ", days)
    sol = Solution()
    sol.maxVacation(flights, days)
    print(Solution.maxDays)
