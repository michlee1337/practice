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
        if len(a) > len(b[x:]):
            return(False)
        subSeq = True
        for i in range(len(a)):
            if a[i] != b[x + i]:
                subSeq = False
                break
        if subSeq:
            return(True)
    return(False)

def isSubInDict(s,d):
    longest = None
    for word in d:
        if isSubSeq(word, s) and (longest is None or len(word) > len(longest)):
            longest = word
    return(longest)

# is a blank string a subseq? can be formed by deletions from b without any reordering so for now I'll assume yes

#_____TESTS_______

print(isSubSeq('','apple'))
print(isSubSeq('app','apple'))
print(isSubSeq('apple','apple'))
print(isSubSeq('ppl','apple'))
print(isSubSeq('ple','apple'))
print(isSubSeq('pplb','apple'))
print(isSubSeq('appleb','apple'))
print(isSubSeq('applebeeeeee','apple'))
print(isSubInDict('apple',['a','ap','ple','pleb']))
# check if s or d is longer to dertermine best method?

# set pointers for all of them and check which pointer can move furthest?
