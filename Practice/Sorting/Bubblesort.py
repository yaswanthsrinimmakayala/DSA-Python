# Non Adaptive 
def bubblesort(arr):
    n = len(arr)
    for i in range(0,n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    return arr

arr = [1,2,9,8,3,2,9,2]
print(bubblesort(arr))

# Adaptive
def adaptive_bubblesort(arr):
    n = len(arr)
    flag = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                flag = 1
        if flag==0:
            break
    return arr

arr = [1,9,8,5,3,4,2,10,11,12]
print(adaptive_bubblesort(arr))


