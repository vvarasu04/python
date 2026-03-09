#Remove duplicate

"""str1=input("Enter the string :")
str2=""
for i in str1:
    str2=i+str2
print(str2) """

#palindrome check
"""str1=input("Enter the string :")
str2=""
for i in str1:
    str2=i+str2
if(str1==str2):
    print("Palindrome")
else:
    print("non palindrome")"""
    
#duplicate remover
"""list1=[1,2,3,3,2,5,6,7]
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)"""

#factorial
"""n=int(input("Enter the number:"))
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

print(fact(n))"""


#vowels counter
"""string1=input("Enter the string: ")
vowels="aeiou"
count=0

for i in string1:
    if i in vowels:
        count+=1
print(count)"""


#frequency check:
string1=input("Enter the String: ")

count={}
for i in string1:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
print(count)
    
    
    




