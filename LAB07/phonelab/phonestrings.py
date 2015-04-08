""" We convert dotted phone numbers like 415.123.4567 or 
YOU.GOT.MILK to phone numbers in standard format.

    >>> phone('YOU.GOT.M1LK')
    '(968) 468-6155'

    See the test files for detailed examples.
"""

from phoneletters import letter2digit, string2digits

DOT = '.'

def phone2string(s):

    """
    >>> phone('415.239.3000')
    '(415) 239-3000'

    >>> phone('YOU.GOT.M1LK')
    '(968) 468-6155'

    """

    s = s.split(DOT)
    TEMPLATE = """({first:}) {second:}-{third:}"""
    return TEMPLATE.format(first=s[0], second=s[1], third=s[2])


def phone(s):

    return string2digits(phone2string(s))



