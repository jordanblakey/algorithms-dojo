import re
def textin(str):
    # Given a string, replaces 'two', 'too' and 'to' with the number '2'.
    str = re.compile('two', re.IGNORECASE).sub('2', str)
    str = re.compile('too', re.IGNORECASE).sub('2', str)
    str = re.compile('to',  re.IGNORECASE).sub('2', str)
    return str
