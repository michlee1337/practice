# The code here will ask the user for input based on the askables
# It will check if the answer is known first

import tempfile
import os
#from git import Repo


# Check if pyswip package needs to be installed

from pyswip.prolog import Prolog
from pyswip.easy import *

prolog = Prolog() # Global handle to interpreter

retractall = Functor("retractall")
known = Functor("known",3)

# Define foreign functions for getting user input and writing to the screen
def write_py(X):
    sys.stdout.flush()
    return True

def read_py(A,V,Y):
    if isinstance(Y, Variable):
        response = input(str(A) + " is " + str(V) + "? ")
        Y.unify(response)
        return True
    else:
        return False

write_py.arity = 1
read_py.arity = 3

registerForeign(read_py)
registerForeign(write_py)

prolog.consult("es.pl") # open the KB for consulting

call(retractall(known))
action = [s for s in prolog.query("action(X).", maxresult=1)]
print("Your should " + (action[0]['X'] + "." if action else "unknown."))
