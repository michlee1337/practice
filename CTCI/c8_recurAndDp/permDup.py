# lazy to retype
import permUniq.py

# helper: count duplicates in str
def countDups(str):
    '''
    returns an array of tuples (char, count) of duplicate chars
    '''
    chars = {}
    for c in str:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    # should look for a cleaner way to do this
    return([(key, chars[key]) for key in chars if chars[key] > 1])

# helper: remove certain chars
def stripChars(str, char_list):
    '''
    returns str without any of the chars in char list
    '''
    for c in str:
        if c in char_list:
            str.remove(c)
    return(str)

def permDup(str):
    '''
    returns an array of all unique permutations
    '''
    # base case: if length 1, only with or without
    if len(str) == 1:
        return([str,""])
    # recursive step: break down by character
    else:
         # identify duplicates
         dups = countDups(str)

         # get all possible permutations without duplicate chars
         strippedStr = stripChars(str, dups.keys)
         perms = permUniq(strippedStr)

         #? for simplicity assume one char has duplicates
         #? can only insert after the last position i think
         for char,count in dups:
             # handle one character at a time
             #? memoize, will be repeating
             for i in count:
                 #? i need to get unique combinations of the mini strings, so maybe build up by character?



         # to handle duplicates,
