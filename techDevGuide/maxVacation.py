import sys
import ast

class Solution:
    maxDays = 0
    memo = []

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

        # memo where [i][j] shows max days from i city in j+1 week
        Solution.memo = [[-1 for _ in (enumerate(days[0]))] for _ in enumerate(flights)]
        for i,_ in enumerate(Solution.memo):
            Solution.memo[i][-1] = days[i][0]
        return(self._findMaxVacationDp(flights, days, 0, 0, 0))

    def _findMaxVacationDp(self, flights, days, city, week,curDays):
        # if no more weeks, return curDays
        if week == len(days[0]):
            Solution.maxDays = curDays
            return(curDays)

        # else return corresponding memo (fill if necessary)
        else:
            if Solution.memo[city][week] == -1:
                for i,_ in enumerate(flights):
                    if (i == city or flights[city][i]):
                        possibleDays = days[city][week] + self._findMaxVacationDp(flights, days, i, week + 1, curDays + days[i][week])
                        Solution.memo[city][week] = max(possibleDays, Solution.memo[city][week])
            return(Solution.memo[city][week])

    def _findMaxVacation(self, flights, days, city, week, curDays):
        # base case: if week = last week, end and remember the max value of this path
        if week == len(days[0]):
            Solution.maxDays = max(curDays, Solution.maxDays)
            return(0)
        # recursive step: try all possible path
        else:
            for i,_ in enumerate(flights):
                if (i == city or flights[city][i]):
                    ####if Solution.memo != -1:
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
    print(sol.maxVacation(flights, days))
