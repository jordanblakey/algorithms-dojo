def namelist(names):
# Return: a string formatted as a list of names separated by commas except for the last two names, which should be separated by an ampersand.
    result = ''       
    set = []
    for x in names:
        if x not in set:
            set.append(x)
    if len(set) > 0:
        result += set[0]['name']
        if len(set) > 1:
            for key in set[1:-1]:
                result += ', ' + key['name'] 
            result += ' & ' + set[-1]['name']
    return result

# Or, more succinctly:
def namelist(names):
    if len(names)==0: return ''
    if len(names)==1: return names[0]['name']
    return ', '.join([n['name'] for n in names[:-1]]) + ' & ' + names[-1]['name']
