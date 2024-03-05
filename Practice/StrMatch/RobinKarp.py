def rabin_karp_search(txt,pat):
    t=0
    p=0
    q = 101
    base = 100
    h = 1
    for i in range(len(pat)):
        h  = (h*base)%q
    for i in range(len(pat)):
        t = (base*t + ord(txt[i]))%q
        p = (base*p + ord(pat[i]))%q
    for i in range(len(txt)-len(pat)+1):
        if t==p:
            for j in range(len(pat)):
                if txt[i+j]!=pat[j]:
                    break
                else:
                    j+=1
            if j == len(pat):
                print("Pattern found at index: ",i)
        if i<len(txt)-len(pat):
            t = (base*t- ord(txt[i])*h +ord(txt[i+len(pat)]))%q
            if t<0:
                t = t+q
            
txt = "GEEKS FOR GEEKS"
pat = "GEEK"
rabin_karp_search(txt,pat)