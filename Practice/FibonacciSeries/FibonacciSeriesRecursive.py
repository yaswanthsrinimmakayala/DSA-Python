def fib(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        f = fib(x-1)+fib(x-2)
        return f
    
print(fib(4))
# prints 3 becuase the indexing starts from 0 