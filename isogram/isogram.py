def is_isogram(inputstring):
    string = inputstring.lower()
    for c in string:
        if c.isalpha() == False:
            if c != ' ' and c != '-' and string.index(c) != len(string) - 1 :
                raise Exception("Input error: Only alphabet, spaces and hyphens are allowed.")
                return False
        else:
            if string.count(c) > 1:
                return False
    return True
