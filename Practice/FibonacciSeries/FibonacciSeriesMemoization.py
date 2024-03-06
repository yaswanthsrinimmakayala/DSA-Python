# Recursion - Solve the sub-problems recursively
# Memoization - Store the solution of these sub-problems so that we do not have to solve them again
# Bottom up approach
def fib(x):
    f = [0]*(x+1)
    f[1] = 1
    for i in range(2,x+1):
        f[i] = f[i-1]+f[i-2]
    return f[x]

print(fib(4))

