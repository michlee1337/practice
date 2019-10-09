# Linked List
Benefits
  - add and remove from head in constant time

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
