
#divide and conqueror method

#recursive function for dividing
def merge_sort(arr):
    if(len(arr)==1):
        return arr
    mid=int(len(arr)/2)
    first_half=arr[:mid]
    second_half=arr[mid:]

    return merge(merge_sort(first_half),merge_sort(second_half))

#aggregating(conquering)
def merge(arr1,arr2):
    print(arr1,arr2)
    i=j=0
    merged_list=[]
    while i<len(arr1) and j<len(arr2) :
        if(arr1[i]<arr2[j]):
            merged_list.append(arr1[i])
            i+=1
        else:
            merged_list.append(arr2[j])
            j+=1
    while(i<len(arr1)):
        merged_list.append(arr1[i])
        i+=1
    while(j<len(arr2)):
        merged_list.append(arr2[j])
        j+=1
    return merged_list
    

arr=[23,454,21,34,12,65,5,24]
print(merge_sort(arr))