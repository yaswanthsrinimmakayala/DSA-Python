# In this pruning will take place for already reached cases by pruning

def LCS_m(A,B,m,n,dp):
    if m==0 or n==0:
        return 0
    if dp[m][n]!=-1:
        return dp[m][n]
    if A[m-1]==B[n-1]:
        dp[m][n]=1+LCS_m(A,B,m-1,n-1,dp)
        return dp[m][n]
    else:
        dp[m][n] = max(LCS_m(A,B,m-1,n,dp),LCS_m(A,B,m,n-1,dp))
        return dp[m][n]

if __name__ == "__main__":
    A =  "CARS"
    B =  "THARISNOTACAR"
    dp = [[-1 for j in range(len(B)+1)] for i in range(len(A)+1)]
    result=LCS_m(A,B,len(A),len(B),dp)
    print("The length of longest common subsequence is: ",result)
