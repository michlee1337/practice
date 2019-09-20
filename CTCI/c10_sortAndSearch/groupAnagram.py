import collections

def _sort(word):
    return("".join(sorted(word)))

def groupAnagram(words):
    anagram_dict = collections.defaultdict(list)

    for word in words:
        anagram_dict[_sort(word)].append(word)

    return([v for sublist in anagram_dict.values() for v in sublist])

if __name__=="__main__":
    test_input = (["abt","cabe","tab","ebca","t","bat"],[])
    test_output = (["abt","tab","bat","cabe","ebca","t"],[])

    for i,t in enumerate(test_input):
        x = groupAnagram(t)
        print(x)
        if x != test_output[i]:
            print("Doesn't match!!", test_output[i])
