""" In this module allow sentences to be palindromes.  
    We ignore spaces, punctuation marks, etc. Also, not case-sensitive.

    We define three functions:  stripper, normalize, and is_palindrome.

>>> stripper("Madam, I'm Adam!")≈
'MadamImAdam'

>>> normalize("Madam, I'm Adam!")
'MADAMIMADAM'
>>> normalize("Catch22")
'CATCH'

>>> is_palindrome('Bob')
True
>>> is_palindrome("race car")
True
>>> is_palindrome("A man, a plan, a canal, Panama!")
True

"""

def stripper(s):
    """Removes spaces and non-letters.
    """
    import re
    regex = re.compile('[^a-zA-Z]')
    s = regex.sub('', s)
    return s
   

def normalize(s):
    """Returns the string s as a string consisting only of upper-case letters.
    """

    s = stripper(s).upper()    
    return s


def is_palindrome(sentence):
    """Returns True only if the sentence spells the same backwards,
    when we ignore spaces, upper or lower case, and punctuation marks.
    """
    
    from stringy import is_palindrome
    
    # REPLACE THE pass BELOW WITH YOUR OWN LINES OF CODE
    # TO TEST IT DO ./testrunner at the unix command line
 
    sentence = is_palindrome(normalize(sentence))
    return sentence

"""
[kpekarsk@hills LAB03]$ finger -pms "kpekarsk"
Login     Name               Tty      Idle  Login Time   Office     Office Phone
kpekarsk  Kai Yun Pekarsky   pts/44         Feb 13 13:53 (76.103.88.109)
[kpekarsk@hills LAB03]$ date
Fri Feb 13 14:07:00 PST 2015
"""
