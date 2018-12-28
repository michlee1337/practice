'''
Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appearred in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
'''
# brute force first
# given n is number of chars in S and k is number of words in dict this will take approx O(kn)

# this would be easier if words were stored as a linked list?

#helper func

# check if is subsequence, assuming start at same char
def isSubSeqP(a,b):
    counter = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            return False
    return True

#print(isSubSeqP('appb','apple'))

# check if is subsequence, assuming start at diff char
def isSubSeq(a,b):
    if not a:
        return(True)
    bStartIndex = 0
    for i in range(len(b)):
        if b[i] == a[0]:
            bStartIndex = i
            break
    counter = 0
    for i in range(len(a)):
        if a[i] != b[bStartIndex + i]:
            return False
    return True

# is a blank string a subseq? can be formed by deletions from b without any reordering so for now I'll assume yes

#_____TESTS_______
print(isSubSeq('','apple'))
print(isSubSeq('app','apple'))
print(isSubSeq('apple','apple'))
print(isSubSeq('ppl','apple'))
print(isSubSeq('pplb','apple'))
'''
# find len of a as subseq in b
def lenSubseq(a,b):
    # for char in a, check if it pairs up with a char b
    for iChar in a:
        for jChar in b:
            if iChar == jChar:
                isSubSeq(a[iChar:],b[jChar:])

def longestSubseq(s,d):
    # for each word in dict
    longest = 0
    maxLen = 0
    for word in d:
        # record subseq len
        len = 0
        for iChar in s:
            for jChar in word:
                if iChar == jChar:
                    len += 1
'''

# check if s or d is longer to dertermine best method?

# set pointers for all of them and check which pointer can move furthest?
