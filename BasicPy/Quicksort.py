def quicksort(arr):
    if len(arr)<=1:
        return arr
    
    pivot=arr[0]
    left=[]
    right=[]
    
    for x in arr[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)
            
    return quicksort(left)+[pivot]+quicksort(right)      

arr=[1,2,10,5,6,8,3]
sorted_arr=quicksort(arr)
print(sorted_arr)