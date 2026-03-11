#using count
str1=input("Enter the string: ")
for ch in str1:
    if (str1.count(ch)==1):
        print(ch)
        break 
    
#without using count
str1=input("Enter the string: ")
count={}
for ch in str1:
    count[ch]=count[ch]+1
    
for ch in count:
    count[ch]==1
    print(ch)
    break