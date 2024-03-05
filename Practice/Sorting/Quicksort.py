def swap(a,b):
    temp = a
    a = b
    b = temp
    return a,b
def partition(arr,start,end):
    pivot = arr[start]
    i = start
    j = end
    while i<j:
        while pivot>=arr[i]:
            i+=1
        while pivot<arr[j]:
            j-=1
        if i<j:
            arr[i],arr[j]=swap(arr[i],arr[j])
    arr[start],arr[j]=swap(arr[start],arr[j])
    return j

def quick_sort(arr,start,end):
    if start<end:
        j = partition(arr,start,end)
        quick_sort(arr,start,j)
        quick_sort(arr,j+1,end)

arr = [8,4,5,1,2,9]
quick_sort(arr,0,len(arr)-1)
print(arr)