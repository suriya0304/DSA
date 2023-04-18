def quick(arr):
    if(len(arr)<2):
        return arr
    else:
        pivot=arr[0]
        low=[i for i in arr if i<pivot]
        high=[i for i in arr if i>pivot]
        return quick(low)+[pivot]+quick(high)
    
arr=[23,454,21,34,12,65,5,24]

print(quick(arr))