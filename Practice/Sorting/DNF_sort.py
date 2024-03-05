# Dutch National Flag Algorithm
#Pseudo code:
# if arr[mid] = 
# : 0 swap(mid,low),mid++,low++
# : 1 mid++
# : 2 swap(high,mid),high--

def DNF(arr):
    low = 0
    mid = 0
    high = len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            temp = arr[mid]
            arr[mid] = arr[low]
            arr[low] = temp
            low+=1
            mid+=1
        elif arr[mid]==1:
            mid+=1
        elif arr[mid]==2:
            temp = arr[mid]
            arr[mid] = arr[high]
            arr[high] = temp
            high-=1
    return arr

arr = [0,2,2,1,1,0,0,1,1,2,0,1,2,1,0]
print(DNF(arr))
# by the end the low will point to  1's and high will point to 2's