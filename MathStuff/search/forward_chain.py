from collections import defaultdict
import queue

class DefiniteClause():
    def __init__(self, body, head, inf = False):
        self.body = body
        self.head = head


def fc(kb):

    # ___ INIT ___
    agenda = queue.Queue()
    exp = defaultdict(bool) # expanded, pass
    closed = [] # remember everything that is true

    for c in kb:
        if len(c.body) == 0: agenda.put(c.head)

    # ___ SEARCH ___
    while not agenda.empty():
        p = agenda.get()
        if not exp[p]:
            exp[p] = True
            closed.append(p)
            for c in kb:
                if p in c.body: c.body.remove(p) # simplify clauses
                if len(c.body) == 0: agenda.put(c.head) # update agenda

    return(closed)

S1 = DefiniteClause(["B", "C"],"A")
S2 = DefiniteClause(["D"],"B")
S3 = DefiniteClause(["E"],"B")
S4 = DefiniteClause(["H"],"D")
S5 = DefiniteClause(["G","B"],"F")
S6 = DefiniteClause(["C","K"],"G")
S7 = DefiniteClause(["A","B"],"J")
S8 = DefiniteClause([],"C")
S9 = DefiniteClause([],"E")

kb = [S1,S2,S3,S4,S5,S6,S7,S8,S9]
print(fc(kb))
