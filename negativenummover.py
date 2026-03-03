"""number=[3,4,5,-2,-1,2,8,0,4]

non_negatives =[x for x in number if x>=0]
negatives=[x for x in number if x<0]
rearranged= non_negatives + negatives
print(rearranged)
    """
    
"""    
num = input("Enter a number: ")
reverse_num = ""

for digit in num:
    reverse_num = digit + reverse_num

print("Reversed number:", reverse_num)"""


"""num=input("Enter the number:")
renum=num[::-1]
print(renum)
"""
"""renum=""
num=(input("Enter the number to reverse"))
for digit in num:
    renum=digit+renum
print(renum)"""


"""list1=[1,2,2,1,4,5,6]
list2=[]
for x  in list1:
    if x not in list2:
        list2.append(x)
print(list2)
    """
    
    
"""str1=input("Enter the string:")
str2=''
for letter in str1:
    str2=letter+str2
print(str2)"""


"""rows=5
for i in range(rows,0,-1):
    print(" "*(rows-i)+"* " *(i))
print("")"""

rows=5
num=1
for i in range(0,rows):
    for j in range(i):
        print(num,end="  ")
        num+=1
        
    print(" ")
    
