class animalShelter():
    def __init__(self):
        self.dog_queue = []
        self.cat_queue = []
        self.count = 0

    def enqueue(self,name,species):
        if species == "d":
            self.dog_queue.insert(0,(name, self.count))
            self.count += 1
        elif species == "c":
            self.cat_queue.insert(0,(name, self.count))
            self.count += 1
        else:
            raise ValueError("Species not recognized")

    def dequeueAny(self):
        if len(self.dog_queue) == 0 and len(self.cat_queue) == 0:
            raise ValueError("No animals")
        elif len(self.dog_queue) == 0:
            return(self.cat_queue.pop()[0])
        elif len(self.cat_queue) == 0:
            return(self.dog_queue.pop()[0])
        elif self.dog_queue[-1][1] < self.cat_queue[-1][1]:
            return(self.dog_queue.pop()[0])
        else:
            return(self.cat_queue.pop()[0])

    def dequeueCat(self):
        return(self.cat_queue.pop()[0])

    def dequeueDog(self):
        return(self.dog_queue.pop()[0])

AS = animalShelter()

AS.enqueue("c1","c")
AS.enqueue("d1","d")
AS.enqueue("c2","c")
AS.enqueue("c3","c")
AS.enqueue("d2","d")
print("TEST")
print(AS.dog_queue,AS.cat_queue)
print(AS.dequeueAny()) #c1
print(AS.dequeueCat()) #c2
print(AS.dequeueAny()) #d1
print(AS.dequeueDog()) #d2
print(AS.dequeueAny()) #c3
print(AS.dequeueAny()) #VE

# two layers of DLL

# Cat1
# Dog1
# dog2
# Cat2
# cat3

# cat1  <>  dog1    <>  dog2    <>  cat2   <>     cat3
#                   <>
# <                                  >     <>
