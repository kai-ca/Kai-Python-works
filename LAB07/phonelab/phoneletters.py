"""Phone numbers with letters.

    >>> phone(exchange='P3T', number='FO0D', 
    >>> areacode='N0T')
    '(608) 738-3603'

    See the test files for detailed examples.
"""

from phonenumbers import phone_best

LETTERS = [None, None, "ABC", "DEF", "GHI", 
"JKL", "MNO", "PQRS", "TUV", "WXYZ"]

def letter2digit(letter):
    """Uses phone pad labels to return the 
correspoding digit.
        The digit will be a str object, not an 
int object.

    See the test files for detailed examples.
    """
    
    for i, char in enumerate(LETTERS[2:]):
        if letter in char:
            return str(i+2)
    return letter

def string2digits(s):
    """Convert strings to digits following 
the digits on the phone pad.

    See the test files for detailed examples.
    """

    return ''.join([letter2digit(letter) for letter in s])


def phone(exchange, number, areacode, useperiod=False):
    """Returns the phone number with letters replaced by digits.

    See the test files for detailed examples.
    """

    return phone_best(string2digits(exchange), string2digits(number), string2digits(areacode), useperiod=False)
