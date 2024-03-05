import time
start_time = time.time()
def mm_naive(A,B):
    m = len(A)
    n = len(B[0])
    p = len(B)
    count = 0
    c = [[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(n):
            for k in range(p):
                c[i][j] += A[i][k]*B[k][j]
                count+=1
    return c,count

A = [[1,2,3],[4,5,6]]
B = [[1,2],[3,4],[5,6]]
print(mm_naive(A,B))
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time, "seconds")
print("Number of Multiplications:",mm_naive(A,B)[1])