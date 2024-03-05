# Strassen's Matrix Multiplication algorithm
# consideration it works only for matrices whose dimension is in powers of two
# if not apply padding , remove padding from result
# O(n^2.8)
import numpy as np
def split(x):
    mid = len(x)//2
    return x[:mid,:mid],x[:mid,mid:],x[mid:,:mid],x[mid:,mid:]

def strassen(x,y):
    if len(x)==1:
        return x*y
    else:
        a,b,c,d = split(x)
        e,f,g,h = split(y)
        p1 = strassen(a, f - h)  
        p2 = strassen(a + b, h)        
        p3 = strassen(c + d, e)        
        p4 = strassen(d, g - e)        
        p5 = strassen(a + d, e + h)        
        p6 = strassen(b - d, g + h)  
        p7 = strassen(a - c, e + f) 
        c11 = p5 + p4 - p2 + p6  
        c12 = p1 + p2           
        c21 = p3 + p4            
        c22 = p1 + p5 - p3 - p7  
        c = np.vstack((np.hstack((c11,c12)),np.hstack((c21,c22))))
        return c

def multiply(A,B):# takes input as lists
    A=np.array(A)
    B=np.array(B)
    return strassen(A,B)
    

matrix_A = [ [1, 1, 1, 1], 
            [2, 2, 2, 2], 
            [3, 3, 3, 3], 
            [2, 2, 2, 2] ]   
matrix_B = [ [1, 1, 1, 1], 
            [2, 2, 2, 2], 
            [3, 3, 3, 3], 
            [2, 2, 2, 2] ]

print(multiply(matrix_A,matrix_B))