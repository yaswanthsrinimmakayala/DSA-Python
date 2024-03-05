def insertionsort(arr):
    for i in range(1,len(arr)):
        x = arr[i]
        j = i-1
        while arr[j]>x and j>-1:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = x
    return arr

arr = [8,1,5,2,3]
print(insertionsort(arr))
