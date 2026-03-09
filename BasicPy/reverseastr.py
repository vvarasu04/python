

#using inbuilt method or [::-1]

"""
str1=input("Enter a string to reverse:  ")
str2=str1[::-1]
print(str2)"""



#using for loop char prepending
"""
str1=input("Enter a string to reverse:  ")
str2=''
for ch in str1:
    str2=ch+str2
    
print(str2) """

#using while loop
"""str1=input("Enter a string to reverse:  ")
i=len(str1)-1
str2=''
while i>=0:
    str2=str2+str1[i]
    i=i-1
print(str2)"""

#swap letters using twopointer method

str1=input("Enter the String to Reverse: ")
list1=list(str1)
start=0
end=len(list1)-1

while start<end:
    list1[start],list1[end]=list1[end],list1[start]
    start+=1
    end-=1
str2=''
for i in list1:
    str2+=i
    
print(str2)


    
    


