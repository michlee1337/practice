# https://runestone.academy/runestone/static/pythonds

# 1.10: LIST COMPREHENSION
#    return all unique characters in wordlist

wordlist = ['cat','dog','rabbit']
letterlist = [ch for ch in set("".join(wordlist))]

# 1.11: EXCEPTION HANDLING
#   using try and exept to do something if exception raised
anumber = -10

try:
       print(math.sqrt(anumber))
    except:
       print("Bad Value for square root")
       print("Using absolute value instead")
       print(math.sqrt(abs(anumber)))

#      using raise to throw your own exception
if anumber < 0:
    raise RuntimeError("You can't use a negative number")
else:
    print(math.sqrt(anumber))

# 1.12: FUNCTIONS
#   infinite monkey theorem! "methinks it is like a weasel"

# create random string
def rand(n):
    return(''.join(random.choice(string.ascii_lowercase + ' ') for i in range(n)))

# score accuracy
def acc(s1,s2):
    a = 0
    n = len(s1)
    for x in range(n):
        if (s1[x] == s2[x]):
            a+= 1
    return(a/n)

# repeat until complete (print best attempt every x tries)
def tryTryAgain(s,x):
    m = ''
    b = rand(len(s))
    c = 0

    # return ans if you got it on first try
    if b == s:
        return(b)

    # else try until you get it
    while b!= s:

        # return best attempt every x tries
        if c == x:
            print(acc(s,b))
            print(b)
            c = 0

        # generate random str
        m = rand(len(s))

        # store best str
        if acc(s,m) > acc(s,b):
            b = m

        # increase count
        c += 1

    return(b)

# 1.13: OBJECT ORIENTED PROGRAMMING - CLASSES

class Fraction:

    # __init__ : the constructor function
    #    should be first method defined for any class

    # self is a special parameter that references object itself
    #   must always be first formal parameter
    #   will never be invoked
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print(self.num,"/",self.den)

    # __str__ is called on print(OBJ)
    #    default is to refer to invoked var's address
    #    can be overriden w own function
    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    # Euclid's algo for finding highest common divisor
    def gcd(m,n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

    print(gcd(20,10))

    # overriding default add operator "+"
    def __add__(self,otherfraction):

         newnum = self.num*otherfraction.den + self.den*otherfraction.num
         newden = self.den * otherfraction.den
         common = gcd(newnum,newden)

     return Fraction(newnum//common,newden//common)

    # overriding equal operator "=="
    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

# INHERITENCE: classes can inherit traits from each other (super class, sub class)

# superclass LogicGate
#       it has a method that will be written as we create each logic gate (self.)
class LogicGate:

    def __init__(self,n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output
