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
    return(' '.join(acc))

# Or, more succicntly
def title_case2(title, minor_words=''):
    title = title.capitalize().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])
