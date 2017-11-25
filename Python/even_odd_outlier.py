def iq_test(numbers):
# Take a string of space seperated numbers, and return the index + 1 of the even/odd outlier.
    numbers = [x%2 for x in map(int, numbers.split(' '))]    
    for index, i in enumerate(numbers):
        if numbers.count(i) == 1:
            return index + 1
