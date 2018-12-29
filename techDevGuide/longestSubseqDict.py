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

# determine if it is subsequence, assuming start at diff char

# PROBLEM: what if the same char appears multiple times in b and the subseq is not true at the first occurence but is true at the second
def isSubSeq(a,b):
    # find the starting index for b at which a possible subseq might start
    if not a:
        return(True)
    bStartIndex = []
    for i in range(len(b)):
        if b[i] == a[0]:
            bStartIndex.append(i)
    # for all possible starting indexes, check if a is substring
    for x in bStartIndex:
        counter = 0
        subSeq = True
        for i in range(len(a)):
            if a[i] != b[x + i]:
                subSeq = False
                break
        if subSeq == True:
            return(subSeq)
    return(False)

# is a blank string a subseq? can be formed by deletions from b without any reordering so for now I'll assume yes

#_____TESTS_______
print(isSubSeq('','apple'))
print(isSubSeq('app','apple'))
print(isSubSeq('apple','apple'))
print(isSubSeq('ppl','apple'))
print(isSubSeq('ple','apple'))
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
