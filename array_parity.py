def solve(arr):
    #Given an array of ints, find ints that do not have at least one negative twin.
    acc = []
    for x in arr:
        if -x not in arr: acc.append(x)
    return acc
