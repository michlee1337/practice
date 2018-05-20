# https://runestone.academy/runestone/static/pythonds

# list comprehension:
#    return all unique characters in wordlist

wordlist = ['cat','dog','rabbit']
letterlist = [ch for ch in set("".join(wordlist))]

# exception handling
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
