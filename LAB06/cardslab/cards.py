""" Deck of cards.

    http://en.wikipedia.org/wiki/Standard_52-card_deck

    http://en.wikipedia.org/wiki/Standard_52-card_deck#mediaviewer/File:Piatnikcards.jpg

    Study the test files in the tests directory of this cardslab to learn what exactly
    our functions below are supposed to do.

"""

SUITS_LONG = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
RANKS_LONG = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

# We will use only the first character for suit.
SUITS = [suit[0] for suit in SUITS_LONG]

# To save electrons we will use shorter strings for the ranks.
RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


def deck():
    """A function that uses loops and the lists 
SUITS and RANKS
    to create a list of the 52 cards.

    """
    deck = []
    i = 0
    while i < len(SUITS):
        for number in RANKS:
            deck.append(number+SUITS[i])
        i = i+1
    return deck


def suit(card):
    """Returns the suit of the card."""

    return card[-1:]


def rank(card):
    """Returns the rank of the card."""

    return card[:-1]


def is_ace(card):
    """Returns True only if card is an Ace."""

    return card[:1] == "A"


def value(card, acehigh=True):
    """Returns the value of the card. Jack, Queen , King have values 
11, 12, 13,
    respectively. If acehigh then Ace has 
value 14, otherwise Ace has value 1.
    """

    valueDict = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'NA': 1}
    if card[:-1] in valueDict:
        if not acehigh:
            return valueDict['NA']
        else:
            return valueDict[card[:-1]]
    else:
      return int(card[:-1])

