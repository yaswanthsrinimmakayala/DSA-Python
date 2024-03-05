def linear_search(arr,val):
    for i in range(len(arr)):
        if arr[i]==val:
            return i
    return "Not Found"
arr = [8,5,4,1,2,9]
print(linear_search(arr,9))
print(linear_search(arr,0))