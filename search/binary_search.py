list=[34,56,60,65,72,88,91,93,100]
item=100
low=0
high=len(list)-1
tries=0
while(low<=high):
    mid=(low+high)//2
    print(f"nmber of tries:{tries}\nmid is {list[mid]}")
    if(list[mid]==item):
        print('found')
        break
    if(list[mid]>item):
        high=mid-1
    else:
        low=mid+1
    tries+=1