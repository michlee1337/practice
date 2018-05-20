# https://runestone.academy/runestone/static/pythonds

# list comprehension:
#    return all unique characters in wordlist

wordlist = ['cat','dog','rabbit']
letterlist = [ch for ch in set("".join(wordlist))]
