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


print(intervalScheduling([8,4,2,1],15))

    # do you consider that they have to start at this time?
    # what about dependencies? if task a has to be completed before task b
    #
