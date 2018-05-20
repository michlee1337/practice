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
