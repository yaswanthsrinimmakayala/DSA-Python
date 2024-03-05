def heapify(arr,n,i):
    largest_at = i
    left = 2*i+1
    right = 2*i+2
    while left<n and arr[largest_at]<arr[left]:
        largest_at = left
    while right<n and arr[largest_at]<arr[right]:
        largest_at = right
    if largest_at!=i:
        arr[largest_at],arr[i]=arr[i],arr[largest_at]
        heapify(arr,n,largest_at)
def heap_sort(arr):
    n = len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        heapify(arr,i,0)
    return arr

arr = [8,5,4,1,2,9]
print(heap_sort(arr))