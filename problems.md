# Happy Number
- approach 1: detect and reject loop
  - method: hash map, Floyd Cycle Detection
- approach 2: math
- why is this O(lgn)???

# valid parentheses with wildcard
- brute force < DP < Stack < Greedy
- Stack logic:
  - store stack of open parentheses index and star index
  - balance closing brackets (by popping off open stack then star stack)
  - balance open brackets (by popping remaining vals on open stack off star stack if star index is greater)
- Greedy logic:
  - recognising key variable is balance (the count of unresolved open brackets)
  - recognizing that wildcard just means that you have a set of possible counts
  - recognizing that this set is always contiguous, so you only need to store the endpoints of the range
  - finally at the end, ensure that zero is in range (can break if high is ever less than zero, and there's no logic to low being less than zero).

# Search in rotated array
- identifying the logic specifically
  - the only special case is on "overflow", otherwise functions exactly the same
- the off by one is rough

# Fundamentals
## Tree
- serial/deserial
## DP
- Longest Common Subsequence
- Buy/ Sell Stock
## Greedy
- House Robber
