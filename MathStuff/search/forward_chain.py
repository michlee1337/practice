'''
Implement a forward chaining solver in Python for ascertaining the truth of a symbol given a knowledge base of definite clauses, following the algorithm in Fig 7.15 of Russell & Norvig. You could implement a class called Symbol to represent a logical symbol, as well as a class called DefiniteClause to represent the structure of a definite clause, with a premise set (the body of the clause) and a symbol for the conclusion (the head of the clause). A knowledge base can then be represented as a list of definite clauses. Have your code ready to paste in at the start of class.


'''
from collections import defaultdict

class Symbol():
    def __init__(self, sym):
        self.sym = sym

class DefiniteClause():
    def __init__(self, body, head):
        self.body = body
        self.head = head

def fc(kb, q):
    count = defaultdict(int)
    inferred = defaultdict(bool)
    agenda = []
    for c in kb:
        if c.body = True:
            agenda.insert(0,c)

    while agenda:
        p = agenda.pop()
        if p == q: return (True)
        elif not inferred[p]:
            inferred[p] = True
            for c in kb:
                if p in c.body:
                    count[c] -= 1
                    if count[c] == 0:
                        agenda.insert(0,c)
    return(False)
