def kthLast(node,k):
    # two pointers
    # fast pointer is always k ahead of slow pointer
    # when fast pointer hits the end, return slow

    if node == None or k < 1:
        return(-1)

    s,f = node,node

    # move f pointer k ahead
    for _ in range(k):
        if f.next == None:
            # list too short
            return(-1)
        else:
            f = f.next

    # move both pointers synchronously until f hits the end
    while f.next != None:
        s = s.next
        f = f.next

    return(s.val)


class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

r = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)

r.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8

print(kthLast(None,1))
print(kthLast(r,0))
print(kthLast(r,1))
print(kthLast(r,2))
print(kthLast(r,3))
print(kthLast(r,4))
print(kthLast(r,5))
print(kthLast(r,6))
print(kthLast(r,7))
print(kthLast(r,8))
print(kthLast(r,9))
