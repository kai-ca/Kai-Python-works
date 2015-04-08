def is_word(word):

    file = './sample.txt'
    with open(file,'r') as myfile:
        for word in myfile:
            word = word.strip()
            myfile = list(myfile)
        print(myfile)

        if word == myfile:
            return True
        else:
            return False

is_word('Ada')
