def lcs(x, y):
    # Get the largest common subsequence of two strings

    def subseqs(s):
        # Given an string, returns all subsequences
        seqlen = 1
        pos = 0
        subs = []
        while seqlen <= len(s):
            while pos < len(s):
                if pos+seqlen <= len(s) : subs.append(s[pos:pos+seqlen])
                pos += 1
            pos = 0
            seqlen += 1
        return sorted(set(subs), key=len)[::-1]
        
    
    def consubseq():
        for seq in subseqs(x):
            if seq in subseqs(y):
                return seq
        return ''

    
    def subseq(a,b):
        common = []
        for seq in subseqs(a):
            i = 0
            prevchar = ''
            seencharcount = 0
            fuzzyseq = ''

            for char in list(seq):
                if char in b and seq.index(char) >= seq.index(prevchar):
                    prevchar = char
                    seencharcount += 1
                    fuzzyseq += char
                    if seencharcount == len(seq) : 
                        common.append(fuzzyseq)
                    common.append(fuzzyseq)

        if common != [] : return max(common, key=len)            
        return ''

        
    return max(subseq(x,y), subseq(y,x), key=len)
