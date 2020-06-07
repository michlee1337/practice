
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
    4. Limited ranges of input (can compress to store in constant space, ex english alphabet is 26)

# Heuristics for Solution Design
- Getting the gist of it
  - what is the key variable?
  - can you draw it out? do a few and see if you can find a pattern.
  - what is the question asking? Are there definitions you can use? Can you express it in a different way? ex: as a search problem?
  - is the state changing? along what dimensions?
- Patterns to look out for
  - k-most/ kth = heap (online) or quickselect (faster)
  - k-index = partition
  - find/ guess/ first/ number of = binary search
  - remove/ some kind of adjency relationship/ ranges/ intervals = two pointer
  - search + mutation like anagram/ tracking longest or minimum = hash map
  - tree involved = recursive
  - optimal substructure/ best path = dp
  - nested = stack
  - lookup = hash table (dict)
  - monotonic pattern = stack
  - ordered = queue
  - tuples = graph
  - substr = sliding window
  - generate = backtracking
  - list with one duplicate = cycle detection
- translations
  - max = sum - min
  - x-highest = x index in sorted
  - permutation = same char freq count

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
    - if multiple dimensions, make sure to test cases with mismatched dimension vals (check you're using the right indexes)
- RELATIONSHIP CHECKS
    - equality is == (oops)
    - <, >, is stuff on the right side
    - double check if you should be using < or <=
  - node.val, not node!
- WINDOWS
  - start and end
  - < or <=
  - check edge cases (solution at edge)
- VAR TYPES
  - esp lists of strings of ints!

# Sugar
- to avoid a bunch of if statements
  - make a list of possibilities and iterate through all
    - ex: vectors for directions
- use 0/ infinity in max/ min calcs to handle edge cases within traversal
- multiply to check for matching parity
- while not empty/ not zero: while list/ dict/ int

# Heuristics for best possible
- comparison based sorting algorithms are lower bounded by nlgn
