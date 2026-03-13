#using for loop
"""list1=[1,3,4,5,8,13,14,12,22,19,21]
even=[]
evenc=0
odd=[]
oddc=0
for num in list1:
    if(num%2==0):
        even.append(num)
        evenc+=1
    else:
        odd.append(num)
        oddc+=1
print(f"even numbers are {even} and count is {evenc}")

print(f"odd numbers are {odd} and count is {oddc}")"""

#using while loop
list1=[11,13,42,55,88,13,14,12,22,19,21]
even=[]
evenc=0
odd=[]
oddc=0
i=0
while i<len(list1):
    if(list1[i]%2==0):
        even.append(list1[i])
        evenc+=1
    
    else:
        odd.append(list1[i])
        oddc+=1
    i+=1
print(f"even numbers are {even} and count is {evenc}")

print(f"odd numbers are {odd} and count is {oddc}")
        
    