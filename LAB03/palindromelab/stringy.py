""" In this module any string that spells exactly the same backwards is considered a palindrome.

Examples:

>>> is_palindrome("racecar"), is_palindrome("race car")
(True, False)

>>> is_palindrome("?! 101 !?")
True

>>> is_palindrome("now I won")
True

"""




def is_palindrome(s):
    """Returns True if the string s is the same read backwards.
    """

    return s == s[::-1]
    


