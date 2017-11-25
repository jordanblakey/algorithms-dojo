def solution(string, markers):
    # Given a string and a list of line comment markers, return a string with all comments and trailing whitespace stripped.
    acc = []
    string = string.split('\n')
    for line in string:
        for marker in markers:
            if marker in line:
                line = line[:line.index(marker)]
        acc.append(line.strip(' '))
    acc = '\n'.join(acc)
    return(acc)

# More succinctly:
def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)
