""" As the seeds get bigger we break new records in lenght or in height.

    Usage: import records
    Usage: from records import heightrecords
    Usage: from records import lengthtrecords

>>> lengthrecords(20)
[(1, 1), (2, 2), (3, 8), (6, 9), (7, 17), (9, 20), (18, 21)]

>>> heightrecords(250)
[(1, 1), (2, 2), (3, 16), (7, 52), (15, 160), (27, 9232)]


"""

from triples import triples


def lengthrecords(maxseed):
    """ As the seed goes from 1 to maxseed the hail stones break new length records.
    Return a list of pairs (seed, length) where the length is a new record.
    
    For example:
    
    >>> lengthrecords(20)
    [(1, 1), (2, 2), (3, 8), (6, 9), (7, 17), (9, 
20), (18, 21)]

    """
    
    records = triples(1, maxseed)
    i = 0
    newR = [((records[i][0], records[i][1]))]
    max = records[i][1]

    while i < len(records)-1:
        i = i+1
        if records[i][1] > max:
            max = records[i][1]        
            newR.append((records[i][0], max))    

    return newR


def heightrecords(maxseed):
    """As the seed goes from 1  to maxseed the hail stones break new height records.
    Return a list of pairs (seed, height) where the height is a new record.
   
    For example:

    >>> heightrecords(250)
    [(1, 1), (2, 2), (3, 16), (7, 52), (15, 160), (27, 9232)]
    """
    
    recordsH = triples(1, maxseed)
    i = 0
    newRH = [((recordsH[i][0], recordsH[i][2]))]
    maxH = recordsH[i][2]

    while i < len(recordsH)-1:
        i = i+1
        if recordsH[i][2] > maxH:
            maxH = recordsH[i][2]
            newRH.append((recordsH[i][0],maxH))

    return newRH



if __name__ == '__main__':
    import doctest
    doctest.testmod()
  

