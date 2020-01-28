# [INSERT CODE HERE] Initial state
state = 1

# [INSERT CODE HERE] Define the goal here
goal = 1024

# Frontier
from collections import deque
frontier = deque([state])

# Step counter
steps = 0


while frontier:
    expand = frontier.popleft()

    child1 = 2 * expand
    child2 = 2 * expand + 1

    steps += 1

    if child1 == goal or child2 == goal:
        break
    else:
        frontier.extend([child1,child2])

frontier_size = len(frontier)


print("Breadth-first search terminated after %d steps\n" % steps)
print("Size of frontier at termination is %d" % frontier_size)
