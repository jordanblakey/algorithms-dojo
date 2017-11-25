def maxlen(L1,L2):
    # Given two positive numbers, return the greatest value obtainable by dividing the numbers into 3 equal parts
    lim1 = min([L1, L2])
    lim2 = max([L1, L2])/2
    if max([L1, L2])/3 > lim1: return max([L1, L2])/3
    return min([lim1, lim2])
    
