from collections import defaultdict
import queue

class DefiniteClause():
    def __init__(self, body, head, inf = False):
        self.body = body
        self.head = head


def fc(kb):
    agenda = queue.Queue()
    exp = defaultdict(bool) # expanded, pass
    closed = [] # remember everything that is true

    for c in kb:
        if len(c.body) == 0:
            agenda.put(c.head)

    while not agenda.empty():
        p = agenda.get()
        if not exp[p]:
            exp[p] = True
            closed.append(p)
            for c in kb:
                if p in c.body: c.body.remove(p)
                if len(c.body) == 0:
                    agenda.put(c.head)
    return(closed)
