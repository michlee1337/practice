# Linked List
Benefits
  - add and remove from head in constant time
  - insert in constant time

## Implementation
Node
  - Attributes
    - val
    - pointer to next
    - [pointer to prev]
  - Methods
    - append to tail
Additional Considerations
  - wrap in a LinkedList data structure to keep track of head changes

Actions/ Techniques
  - Deletion
    - check for null
    - update pointers
      - set prev.next = next
      - [set next.prev = prev]
  - Runner technique
      - fast pointer; slow pointer
        - esp useful for midpoints
  - Often requires recursion  

# Arrays
- access any _index_ in constant time
- insertion is O(n)
- ordered

# Queues
Applications
  - BFS and cache
  - maintain order

# Stacks
Applications
- When you just need to compare adjacent elements
- reversal

# Heap
- python heapq
- min/max peek constant time
- min/max pop and insertion is lg(n)
- heap property: parent >/< then child


# Considering Inputs
Limited input set
- ex: max alphabet characters is 26. Could possibly use this to make constant space/ time

# Trip Ups
- duplicate values! Esp with lookup tables
- binary trees != binary search trees
- edge cases: 0,1, None, boundaries
- recursion is not constant space
- search: update and traversal order! Often update before traverse.

# Recursion
- whenever you have optimal substructure
- always consider bottom up (save stack space)

# Backtracking
- Use case
    - Graph search
    - When there are multiple decision points
- Main Concept
    - Try all choices at a decision point
- Implementation
    - Non recursive
        - Path (Remember solution)
        - Seen (Prevent infinite loops)
        - Options (next options to try)
        - [Current (current decision point) ]
    - Recursive (Implicit)
        - Call on all options
        - Make Solution based on returns

# Kanade's (Maximum subarray)
- max at index i is max(s[i], maxSubarr(s[:i]) + s[i])

# Heuristics for Time complexity
- sorted: O(lg) O(1)

# Substr
- sliding window

# Array/ Tree/ List
- often recursion
  - always focus on a node (operations are on a node)
- what type of traversal do you need?

## weaknesses
- trees, parents and children (what to do without parent connections)
  - work with children

## serialize/ deserialize a tree
- serialize: if none x, do left do self do right
- deserialize: if x, none and return, do left do self do right

# BST
- use the BST property
- left child is <, right child is >

# Techniques
- Always try recursion first C:
  - Makes it way easier haha
- Base case and build
  - Trivial solution?
  - Reducing Step?
- Pen and paper
  - solve in life
  - find patterns/ steps
- breakdown components you need
  - variables we need (two moving variables? pointers/ temp?)
- if stuck: what other way can I get the information that I need? how are the variables/ components related? can I tell information X from A rather than B? How is X created? What is it related to
- Reverse?
  - stack
- comparing adjacent?
  - stack
- maintain and traverse in order?
  - queue
- max continuous/ path in one pass?
  - maintain globalMax; currentMax
- flipping between cases?
  - max/min; negative/positive
  - store what you need for both cases; a boolean flag state
- dp: memoizing
  - what is the problem structure? whats repeated?
  - what dimensions along which do the problems change? how do they match?
- if traversing/ searching graph/ Backtracking
  - lookout for loops. use a seen lookup.

# Bits
- x&(x-1) flips the last 1 to 0

# Dutch Partitioning Problem (partition 3)
- pointer to each partition
- swap pointer values as necessary and increment pointers

# Questions
## Stock
- buy/sell once:
  - max subarray on changes (kanade)
- buy/sell multiple times
  - Shortcut greedy:
    - max is just the sum of all the differences price[j] - price[i] where j > i
    - compare by pairs of days (you can "sell than buy again" on a day, equivalent to holding, but the profit is still the breakdown by pairs of days)  
  - DP:
    - best\[num days to transact][num items in hand (here, limited to binary 0 or 1)]
    - to save space, since every row solution is only based on the last row, you can store the vars best_with and best_without stock
    - for price in prices:
      - best_with = max(best_with, best_without-price)
      - best_without = max(best_without, best_with-1)
    - return(best_without)
- buy/sell k times:
  - DP: build up by <num transactions <total days>>, guess which day the last transaction completed
  - memo[i][j] = max profit w i transactions remaining and selling on jth day
  - Base Cases:
    - memo[0][j] = 0 # no possibility of selling w no transactions
    - memo[i][0] = 0 # can't sell on first day
  - for i in range(k) # build up by transaction
    - for m in prices range(0,j-1) # guess the day
        - memo[i][j] = max(memo[i][j-1],price[j]-price[m]+memo[i-1][m])

# Kth Smallest
- algorithm
  - min heap of elements from the first breakdown
    - + row and col number
  - k times
    - get min element from min heap
    - replace root w the next element from same col and min heapify
    - return last extracted root
- intuition
  - take advantage of the sorted, while sorting between cols
  - need to sort within cols = need to maintain some sorted structure of cols
  - sorted cols = always only need to check top col

switch between two "threads of logic"
- two recursive functions, one calls the other
  - less checks at each stage

# KMP
- Problem: pattern matching a term t in a string s
- Key: take advantage of successful character matches
- Application: Find a suffix (of matched subterm) that is also a prefix
  - optimise by building a prefix suffix table
    - list element i tells us the longest prefix suffix match for substring t[:i]

# Graph

## Djikstra
- find shortest path tree
- greedy
- DP: keep a priority queue of minimum distance to each path from start node
  - init
    - with 0 for start node, infinity for all others
    - mark all nodes as unexplored
    - mark parents as unknown
  - while not goal
    - process top of priority queue
    - update all children of nodes adjacent with best path (distance + parent)  

## Prim's
- find minimum spanning tree
  - connect all nodes, with minimum total cost
- greedy
- consider all edges reachable from currently reachable nodes
- while not all nodes reachable
  - choose the minimum
  - remove all edges that connect two already reachable nodes
  - update edges reachable

# Pretty
- memoize with a decorator :)

min path: uniform cost search (if admissable)

# Bit Manipulation

## XOR
- XOR of a number with itself is 0
- XOR of a number with 0 is the number itself
- XOR is commutative so the order of numbers does not matter

### Sample Problems
#### Find number without a pair in a list
- you can figure out the parity of each bit by looking at the parity (the one w odd parity will be the unique)
- you can figure out the parity of each elemnt in the binary rep w an xor

# Pointers
- Floyd Cycle Detectio
  - ref: https://www.youtube.com/watch?v=LUm2ABqAs1w
  - algorithm
    - check loop: fast pointer moves 2s, slow pointer moves 1s
    - find start of loop: move one pointer to the front, move both 1s until they meet at the starting node of the loop
  - proof
    - l = loop_length
    - k = distance from loop-start_node to meeting_node
    - m = distance from problem-start_node to loop-start_node
    - fast = m + p*l + k # p = num cycles of fast
    - slow = m + q*l + k # q = "" slow
    - fast = 2*slow
    - simplifies to m+k = l(p-2q)
    - the reset pointer moves m (to start of loop), the remaining pointer that was at k moves as additional m which places it back at the start node as well.

# DP
## Tips
- try to build on the simplest possible subproblem (if you can build from only one subproblem do it)
  - ie: try to come up with a linear brakdown
  - with monotonous things (like sums), this is normally possible
