def binary_search(arr,x):
    low = 0
    high = len(arr)-1

    while low<=high:
        mid = (low+high)//2
        if arr[mid]==x:
            return mid
        elif x < arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return -1

arr=[76, 9, 90, 65, 7, 91]
x=90
res=binary_search(arr, x)
if res==-1:
    print("Element is not found")
else:
    print("The element is found at index", res)
