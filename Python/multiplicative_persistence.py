def persistence(n):
#Takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
    result = 0
    while len(str(n)) > 1:
        n = reduce(lambda x, y: x*y, map(int, (str(n))))
        result += 1
    return result
