def glm(arr):
    #  returns positions and values of local maxima in a list.
    p = [{'pos': [], 'peaks': []}]
    def cp():
        p[0]['pos'].append(i)
        p[0]['peaks'].append(x)
    for (i, x) in enumerate(arr):
        if not (i == 0 or i == len(arr) - 1):
            if cmp(x, arr[i - 1]) > 0 and cmp(x, arr[i + 1]) >= 0 and len(set(arr[i:])) != 1:
                if cmp(x, arr[i + 1]) == 0:
                    for j in arr[i:]:
                        if j > x: break
                        if j < x:
                            cp()
                            break
                else: cp()
    return p[0]
