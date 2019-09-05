# breakdown

# store starting height
## as long as the following heights are lower, stay (add to volume)
### following heights higher, end and new start (recorded collected volume)

class Solution:
    def lakeVolume(terrain):
        # O(n) time
        # O(n) space

        # init storage variables
        p_start = -1
        p_floor = []

        t_capacity = 0

        # calculate capacity
        for elevation in terrain:
            if elevation > p_start:
                # add capacity and reinit pool
                t_capacity += sum([(min(p_start, elevation) - e) for e in p_floor])
                p_start = elevation
                p_floor = []
            else:
                # update pool width
                p_floor.append(elevation)

        # deal with last pool
        if p_floor != []:
            terrain = p_floor[::-1]
            terrain.append(p_start)
            # init storage variables
            p_start = -1
            p_floor = []
            # calculate capacity
            for elevation in terrain:
                if elevation > p_start:
                    # add capacity and reinit pool
                    t_capacity += sum([(min(p_start, elevation) - e) for e in p_floor])
                    p_start = elevation
                    p_floor = []
                else:
                    # update pool width
                    p_floor.append(elevation)
        if p_floor != []:
            t_capacity += sum([(min(p_start, elevation) - e) for e in p_floor])
            p_floor = []

        return(t_capacity)

if __name__ == "__main__":
    terrain = [int(x) for x in input("terrain: ").split()]
    print(Solution.lakeVolume(terrain))
