""" BONUS01:cyclelab  CS131A Python Programming. Spring 2015.  
    Copyright (c) 2015. Ulf Wostner <wostner@cyberprof.com>. 
    All rights reserved. Do not share, post, or distribute in any form.

    This BONUS assignment is challenging. You need to do some research and reading to figure out 
    what methods are needed to get the behavior we want of Cycle objects.

    Read the lecture notes and the textbook first.

This is cyclelab where you define a class named Cycle.

   Starting with a list of items we create an instance of Cycle.

    >>> SEASONS = ['Spring', 'Summer', 'Fall', 'Winter']

    >>> seasons = Cycle(SEASONS)

    >>> isinstance(seasons, Cycle)
    True

    >>> seasons.item()
    'Spring'
    >>> seasons.rotate()
    >>> seasons.item()
    'Summmer'




GAMEPLAN:

    Read the tests in tests/testA.txt
    Write code in cycle.py until tests/testA.txt is OK.

    Read the tests in tests/testBtxt
    Write code in cycle.py until tests/testB.txt is OK.

    Read the tests in tests/testC.txt
    Write code in cycle.py until tests/testC.txt is OK.

    

PROGRAMS BY:

    Login     Name               Tty      Idle  Login Time   Office     Office Phone
    kpekarsk  Kai Yun Pekarsky   pts/17         Mar 20 15:38 (76.103.88.109)


DATE SUBMITTED:
    
    Fri Mar 20 16:35:13 PDT 2015


HOW TO SUBMIT YOUR COMPLETED LAB:

        (0) EDIT this __init__.py file to replace the two lines above marked by ***.  That's 10 points, folks.

        (1) Make sure that all tests run without errors. Otherwise the lab is not completed.

        (2) As usual, create a tarball of the lab.
        
        (3) Reply to this email on hills using pine.  Attach the tarball.

        (4) DUE DATE: Monday, March 24, 2015 at 11:59 pm.

"""

