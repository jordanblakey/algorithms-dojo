def list_items(items):
    # Given a list of strings, return a formatted, ordered list.
    list = ''
    for i, x in enumerate(animals):
        list += str(i+1) + '. ' + x + '\n'
    print(list)
    return list

# Refactored:
def list_items2(items):
    list = ''
    for i, x in enumerate(animals): list += str(i+1) + '. ' + x + '\n'
    return list
