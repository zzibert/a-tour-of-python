from random import shuffle

words = ['one', 'two', 'three', 'four', 'five']

def jumble(word):
    anagram = list(word)
    anagram.reverse()
    return "-".join(anagram)
    
print([ jumble(w) for w in words])

