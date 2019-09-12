import collections

class IF:
  def __init__(self, iterlist):
      self.iterlist = collections.deque(iterlist)

  def __next__(self):
      iter = self.iterlist.popleft()
      try:
          print(next(iter))
          self.iterlist.append(iter)
          return(0)
      except:
          pass

  def hasNext(self):
      return(len(self.iterlist) != 0)

if __name__=="__main__":
    l1 = [1,2,3]
    l2 = ["a","b"]
    l3 = "applebee"
    i1 = iter(l1)
    i2 = iter(l2)
    i3 = iter(l3)

    ix = IF([i1,i2,i3])
    while ix.hasNext():
        next(ix)
