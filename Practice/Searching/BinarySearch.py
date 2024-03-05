def binary_search(arr,val):
    l = 0
    r = len(arr)-1
    while l<=r:
        mid = (l+r)//2
        if arr[mid]==val:
            return mid
        if arr[mid]<val:
            l = mid+1
        if arr[mid]>val:
            r = mid-1
    return "Not Found"

arr = [1,2,3,4,5,6,7,8]
print(binary_search(arr,val=8))
