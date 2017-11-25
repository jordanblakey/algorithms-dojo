def validBraces(string):
    # Takes a string of braces, and determines if the order of the braces is valid. Return true if the string is valid, and false if it's invalid.
    string = list(string)
    o = [0,0,0]
    for char in string:
        if char is '(': o[0] +=1
        if char is ')' and o[0] < 1 : return False
        if char is ')': o[0] -=1

        if char is '[': o[1] +=1
        if char is ']' and o[1] < 1 : return False
        if char is ']': o[1] -=1
        
        if char is '{': o[2] +=1
        if char is '}' and o[2] < 1 : return False
        if char is '}': o[2] -=1
        print('po:',o)
    if o[0] != 0 : print('paren error.'); return False
    if o[1] != 0 : print('square error.'); return False
    if o[2] != 0 : print('curl error.'); return False
    return True
    
