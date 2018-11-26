def intervalScheduling(times, interval):
    '''
    Return largest set of mutually compatible activities within a set time frame considering their durations.
    '''
    executed = []
    # while time is more than the minimum activty
    while interval >= min(times):

        # find longest activity within time frame
        longest = max(times)
        while longest > interval:
            times.remove(longest)
            longest = max(times)

        # execute activity
        executed.append(longest)
        interval -= longest
    return(executed, interval, times)

def intScheduling(meetings, interval):
    executed = []
    while len(meetings) > 0:
        start_times = []
        end_times = []

        for times in meetings:
            start_times.append(times[0])
            end_times.append(times[1])

        # take earliest ending time
        best = end_times.index(min(end_times))

        # if no meetings left possible, end
        if meetings[best][1] > interval:
            return(executed, interval, meetings)

        # else execute
        else:
            executed.append(meetings[best])
            last_time = meetings[best][1]
            meetings.pop(best)

        # remove all meetings made impossible
        poss_meetings = meetings
        for time in meetings:
            if time[0] <= last_time:
                meetings.remove(time)
    return(executed, interval, meetings)

print(intScheduling([[2,4],[8,12],[2,15]],15))

    # do you consider that they have to start at this time?
    # what about dependencies? if task a has to be completed before task b
    #
