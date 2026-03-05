string1=input("Enter the string")
num={}

for ch in string1:
    if ch in num:
        num[ch]=num[ch]+1
    else:
        num[ch]=1 
        
print(num)   