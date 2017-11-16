def nbr_of_laps(x, y):
    ''' 
    Given the integer length of two joggers laps running the same speed and starting at the same time, 
    returns a list of how many laps each jogger will run befor seeing the other. 
    '''
    iter = 1
    while iter < 1000000000:
        if x * iter % y == 0: return [iter, int((x * iter)/y)]
        iter += 1

# The mathy way
def nbr_of_laps(x,y):
    def gcd(a,b):
        while b:
            a,b = b,a % b
        return a
    def lcm(a,b):
        return a*b // gcd(a,b)
    return [lcm(x,y/x)/x, lcm(x,y),y]
