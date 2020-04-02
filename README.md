#! to review
!! i still don't get the increasing substring q
? is setting a whole row faster than setting each element?
!? why doesn't the factor approach work for sqrt
? how to know when to use binary search (sqrt q)
  - searching in one dimension
! learn graphs and search/ traversal better
!! I think i need to do an algorithms course :P

!! with recusive/ search problems (often searches are recursive problems)
- find a dimension you can break down along
  - ex: longest subarray: subarrays of len x
  - watch .006 on DP
!! Greedy: see if its possible. strictly increasing/ monotonous things normally make it possible
!! get familiar w bfs vs dfs in perms and other scenarios
?? How can I tell when the entire search space needs to be searched? no heuristic? (ex: coin change)
______

# General Approach
1. Clarify
    1. Inputs
    2. Outputs
    3. One walkthrough example: so X returns Y?
    4. Edge cases?
    5. draw out the problem
3. Formulate approach
    1. Brute force
    2. What is the core thing that needs to be mutated/ changed?
    3. If I write it out and solve a couple by hand, can I find a pattern?
    4. Is there a base case I can identify and then build on?
    5. Can I break this down into multiple pieces I can work on individually?
    6. What data structures might be relevant?
    7. Best conceivable runtime?
4. After getting ok from interviewer, start coding
  1. Keep a list of things you need to do (forgetful child)
  2. Double check conditions and things to do
5. Test with edge cases + debug
6. Time complexity + space complexity
7. Optimize
    1. Bottlenecks (longest time step)
    2. Unnecessary work (avoid)
    3. Repeated work (caches)

# Gotchas
- UNDERSTANDING
  - what inputs does it take
    - don't assume!!
    - sorted?
    - edge case?
  - what type should the func return (int count? array?)
  - what should the func return if empty input?
- DESIGNING SOLUTION
  - [if base case] What should base case be, 0 or -inf?
  - infinite loops (increasing counter?)
  - check index bounds (not less than 0, not more than length)
  - handle edge cases!
  - try not to overcomplicate! if stuck. pause for a second.
- TRAVERSALS
  - loops
- RANGES
  - from i to j is range(i:j+1)
- EDGE CASES
  - empty inputs
  - duplicates (when searching/ sorting/ storing)
  - negative numbers
  - zeros/ duplicates of zeros
- HELPERS
  - if declaring helpers, make sure to not confuse helpers with main, and call/define w self if necessary
  - if changing params/name, check all instances
- INDEXES
    - stop when >= len()
    - off by one
    - confusing between pointers/ indexes
    - concat vs append
    - careful with 2d arrays (brackets + index order)
    - ind (starting from 0 or 1), esp memo
    - if segmenting by indexes, remember the diff between 0 and sInd, -1 and eInd
    -
  - EQUALITY CHECKS
    - equality is == (oops)
    - <, >, is stuff on the right side
  - node.val, not node!

# General Knowledge/ Hueristics
- comparison based sorting algorithms are lower bounded by nlgn

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
- buy/sell once: max subarr
- buy/sell multiple times: while decreasing, switch buy. while increasing, switch sell. repeat.
- buy/sell k times:
  - memo[i][j] = max profit w i transactions remaining and selling on jth day
  - for m in prices range(0,j-1)
    - # max no activity vs max profit buying on day m, selling on day j, + profit before day m
    - memo[0][j] = 0 # no possibility of selling w no transactions
    - memo[i][0] = 0 # can't sell on first day
    - memo[i][j] = max(memo[i][j-1],price[j]-price[m]+memo[i-1][m])
      - # max of not doing anything vs profit buying on m, selling on j + profit with one less transaction ending before m day

# Design Patterns
- Composition over Inheritence
  - take state as function parameters.
  - "Has a" vs "Is a", but favor composition

# Java
- static typing
- structure through braces and semicolons
- No dictionary! Map
- char -> int: Character.getNumericValue()
- for loop: for(var i; i<ending_condintion,increment){};
- no nested functions
- Change string to char array: .toCharArray();
- indexing strings: .charAt(i);


# Kitchen Sink
- list index == num smaller than
- sort one list by another
  - lambda sort, or dict lookup
- dicts: setdefault
- List
  - split each char List(s)
  - split by seperator s.split(<sep>)
  - when indexing, always check for empty first
- custom comparator: neg = left first
- how to convert comp to key?
- join is a _string_ method!
- tree? recurse
- always forget: _duplicatessss_
- always check none
- trees: careful w comp parent or child
- backtrackinggggg
- level order traversal: pre traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/114449/A-general-approach-to-level-order-traversal-questions-in-Java

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
