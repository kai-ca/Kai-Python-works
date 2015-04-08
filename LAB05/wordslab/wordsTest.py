"""We read words from a file on hills that has almost half a million words.
We accept any line in that dictionary as a word.

>>> is_word('radar')
True
>>> is_word('Ada')
True
>>> is_word('Turing')
True
>>> is_word('hand-fed')
True

Our is_word is not case-sensitive.

>>> is_word('mESsY')
True

We create a set consisting of all the words, but written in lower-case.

For efficiency we keep go by word size. So, wordset(n) has all words of length n.

Remember that they are changed to lower-case.

>>> 'Turing' in wordset(6)    
False

>>> 'turing' in wordset(6)
True


Read the file tests/test_words.txt to see what we want from our is_word and wordset.

"""

HILLSDICTFILE = '/usr/share/dict/words'

def is_word(word):
    """Is the word in the hills dictionary?
        Allows any characters used in the hills dictionary words.
        Not case-sensitive.
    """
    with open(HILLSDICTFILE, 'r') as f:
        for line in f:
            words = line.strip().lower()

    return word.lower() == words


def wordset(size):
    """Returns a set, not a list, with all the words of that size from the hills dictionary.
       All words are changed to lower-case before added to that set.
    """
    myset = set()
    with open(HILLSDICTFILE, 'r') as f:
        for line in f:
            word = line.strip()
            word = word.lower()
            if size == len(word):
                myset.add(word)
    
    return myset
