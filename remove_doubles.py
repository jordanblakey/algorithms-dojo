def doubles(s):
    # given a string, sequentially remove adjacent character pairs
    for c in s: s = s.replace(c+c, '')
    return s
