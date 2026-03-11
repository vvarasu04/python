#Basic method using Count()
"""str1=input("Enter the string:")
for ch in str1:
    if(str1.count(ch)==1):
        print(ch,end=" ")"""
        
#Method without using count 
str1=input("Enter the string:")
count={}
for ch in str1:
    count[ch]=count.get(ch,0)+1
    
    
for ch in str1:
    if count[ch]==1:
        print(ch)
    