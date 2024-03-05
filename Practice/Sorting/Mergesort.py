def merge(arr,start,mid,end):
    B=[]
    i = start
    j = mid+1
    while i<=mid and j<=end:
        if arr[i] < arr[j]:
            B.append(arr[i])
            i+=1
        else:
            B.append(arr[j])
            j+=1
    while i<=mid:
        B.append(arr[i])
        i+=1
    while j<=end:
        B.append(arr[j])
        j+=1

    for inx,val in enumerate(B):
        arr[inx+start] = val

    return arr

def merge_sort(arr,start,end):
    if start<end:
        mid = (start+end)//2
        merge_sort(arr,start,mid)
        merge_sort(arr,mid+1,end)
        arr=merge(arr,start,mid,end)
        return arr

arr = [8,5,4,1,2,9]
print(merge_sort(arr,0,5))