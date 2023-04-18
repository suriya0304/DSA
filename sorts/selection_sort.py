def find_smallest(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range(1,len(arr)):
        if(smallest>arr[i]):
            smallest_index=i
            smallest=arr[i]
    return smallest_index
    
def selection_sort(new_arr):
    for i in range(len(arr)):
        smallest=find_smallest(arr)
        new_arr.append(arr.pop(smallest))

arr=[23,454,21,34,12,65,5,24]
new_arr=[]
selection_sort(new_arr)
print(new_arr)