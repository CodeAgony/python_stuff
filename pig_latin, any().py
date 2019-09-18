def has_numbers(word):
    return any(char.isdigit() for char in word)

def pig_latin(word):
    """Returns a simplified Pig Latin version of received word"""
    if has_numbers(word):
        print("Pig Latin doesn't work numbers, sorry")
    elif word[0] in ('e','a','i','o','u'):
        print("{}way".format(word))
    else:
        print("{}{}ay".format(word[1:],word[0]))

pig_latin('owl')

