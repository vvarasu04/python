#using loop
"""lst=[1,2,3,0,4,0,5,0,6]
result =[]
count=0
for num in lst:
    if  num !=0:
        result.append(num)
    else:
        count+=1
for i in range(count):
    result.append(0)
    
print(result)"""

#using two pinter method
arr=[1,2,0,3,0,4,0,5,7,8]
j=0
for i in range(len(arr)):
    if arr[i] !=0:
        arr[j],arr[i]=arr[i],arr[j]
        j=j+1
print(arr)
        
