""" We study words from the hills dictionary that form a different word when read backwards.

>>> is_reword('reward')
True

No palindromes allowed this time.

>>> is_reword('rotor')
False

Case will be ignored.

>>> is_reword('Pat')
True
>>> is_reword('turtle')
False


How many rewords of length eight?

>>> len(rewordset(8))
10

"""

from words import HILLSDICTFILE
from words import is_word, wordset



def is_reword(s):
    """Returns True only if s and s backwards are different words in the hills dictionary.
    """
    
    revS = s[::-1]

    return is_word(revS) and revS.lower() != s.lower()


def rewordset(size):
    """Returns a set with all 'rewords' of that size from the hills dictionary.
    All words are in lower-case and none are palindromes.
    """
    
    myrevset = set()
    hillset = wordset(size)
    for word in hillset:
        revW = word[::-1]
        myrevset.add(revW)

    newset = set()
    for word in myrevset:
        if word in hillset:
            newset.add(word)

    return newset

