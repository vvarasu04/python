"""nums=[1,2,3,1,2,3,5,4,6,7,7,4]
unique=[]
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)"""

"""nums=[1,2,3,1,2,3,5,4,6,7,7,4]
unique=list(set(nums))
print(unique)"""

"""nums=input("Enter the numbers with space:").split()
unique=list(set(nums))
print(unique)"""

"""nums=input("Enter the numbers with space:").split()
unique=[]
for i in nums:
    if i not in unique:
        unique.append(i)
print(unique)"""

val=[1,2,3,4,3,2,5,6]
unq=[]
for i in val:
    
    if i not in unq:
        unq.append(i)
print(unq)