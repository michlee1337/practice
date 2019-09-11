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

        # memo where [i][j] shows max days from i city in j+1 week
        Solution.memo = [[-1 for _ in (enumerate(days[0]))] for _ in enumerate(flights)]

        for i,_ in enumerate(Solution.memo):
            Solution.memo[i][-1] = days[i][-1]
        self._findMaxVacationDp(flights, days, 0, -1, 0)
        return(max([city[0] for city in Solution.memo]))

    def _findMaxVacationDp(self, flights, days, city, week,curDays):
        # if just starting, search all cities
        if week == -1:
            for i,_ in enumerate(flights):
                if (i == city or flights[city][i]):
                    possibleDays = self._findMaxVacationDp(flights, days, i, 0, 0)
                    Solution.memo[i][0] = max(possibleDays, Solution.memo[i][0])

        # else return corresponding memo (fill if necessary)
        else:
            if Solution.memo[city][week] == -1:
                for i,_ in enumerate(flights):
                    if (i == city or flights[city][i]):
                        possibleDays = days[city][week] + self._findMaxVacationDp(flights, days, i, week + 1, curDays + days[i][week])
                        Solution.memo[city][week] = max(possibleDays, Solution.memo[city][week])
            return(Solution.memo[city][week])

if __name__=="__main__":
    flights = ast.literal_eval(sys.argv[1])
    days = ast.literal_eval(sys.argv[2])
    print("flights: ", flights)
    print("days: ", days)
    sol = Solution()
    print(sol.maxVacation(flights, days))
    #print(Solution.memo)
