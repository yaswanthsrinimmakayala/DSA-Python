# Using Tablation
def LCS_T(A,B):
    m = len(A)+1
    n = len(B)+1
    LCS = [[None]*(n) for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i==0 or j==0:
                LCS[i][j] = 0
            elif A[i-1]==B[j-1]:
                LCS[i][j] = 1+LCS[i-1][j-1]
            else:
                LCS[i][j] = max(LCS[i][j-1],LCS[i-1][j])

    return LCS[m-1][n-1]

if __name__=="__main__":
    A = "INTENTION"
    B = "EXECUTION"
    result = LCS_T(A,B)
    print("The length of LCS: ",result)