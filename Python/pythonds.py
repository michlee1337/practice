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
# this is a IS-A relationship

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

# sub class: inherits from a superclass
class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        return int(input("Enter Pin A input for gate "+ self.getLabel()+"-->"))

    def getPinB(self):
        return int(input("Enter Pin B input for gate "+ self.getLabel()+"-->"))

    def setNextPin(self,source):
    if self.pinA == None:
        self.pinA = source
    else:
        if self.pinB == None:
            self.pinB = source
        else:
           raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):

    def __init__(self,n):

        # can replace explicit call to parent(s) with super
        # ex: super(UnaryGate,self).__init__(n).
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.getLabel()+"-->"))

class AndGate(BinaryGate):

    def __init__(self,n):
        super(AndGate,self).__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

# connectors have a HAS-A relationship
# they have instances of logic gate class within the,but are not part of the hiarchy

class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

# RECURSION
# 1) base called
# 2) must change state towards base case
# 3) must call itself recursively

# function to return the numbers in their binary versions

def addition(nList):
    if len(nList) == 1:
        return (nList[0])
    else:
        return (nList[0] + addition(nList[1:]))

def base2(n):
    # can be broken up into (dividend%2) + n/%2

    # base case: n<2
    if(n<2):
        return(n%2)

    # (dividend%2) + n/%2
    else:
        return(str(base2(n//2)) + str(n%2))

# reverse string w recursion
def reverse(s):
    # can be summrised into s[-1] + restOfList[-1]
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverse(s[:-1])

# check for palindroms with RECURSION
def isPal(s):
    # compare first and last word recursively
    if len(s) <= 1:
        return True
    elif s[0] != s[-1]:
        return False
    else:
        return isPal(s[1:-1])
    return False
