def kmp(txt,pat):
    M = len(pat)
    N = len(txt)

    lps = [0]*M
    lps_array(pat,lps)
    i=0
    j=0
    while N-i>=M-j:
        if txt[i]==pat[j]:
            i+=1
            j+=1
        if j==M-1:
            print("Pattern found at index:",i-j)
            j=lps[j-1]
        elif i<N and txt[i]!=pat[j]:
            if j!=0:
                j=lps[j-1]
            else:
                i+=1

def lps_array(pat,lps):
    M=len(pat)
    length=0
    i=1
    while i<M:
        if pat[i]==pat[length]:
            length+=1
            lps[i]=length
            i+=1
        else:
            if length!=0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i+=1

txt = "ABABDABACDABABCABABABABCABAB"
pat = "ABABCABAB"
kmp(txt,pat)