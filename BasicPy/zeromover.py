lst=[1,2,3,0,4,0,5,0,6]
result =[]
count=0
for num in lst:
    if  num !=0:
        result.append(num)
    else:
        count+=1
for i in range(count):
    result.append(0)
    
print(result)