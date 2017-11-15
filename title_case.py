def title_case(title, minor_words=''):
    # Takes a string and an optional list of exceptions and return a title cased string, ignoring exceptions
    title = title.split(' ')
    minor_words = minor_words.split(' ')
    acc = []
    for i, word in enumerate(title):
        if word.lower() in [word.lower() for word in minor_words] and i != 0:
            acc.append(word.lower())
        else:
            acc.append(word.capitalize())
    print(' '.join(acc))
    return(' '.join(acc))
    
title_case('a clash of KINGS', 'a an the of')
title_case('THE WIND IN THE WILLOWS', 'The In')
title_case('the quick brown fox')
