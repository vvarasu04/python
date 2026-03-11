#
"""str1="abcdefadbfqwq"
str2=''
for i in str1:
    if(i not in str2):
        str2=str2+i
print(str2)"""


#using set

"""str1="abcdefadbfqwq"
str2=set(str1)
print(sorted(str2))"""


#using list method
"""str1=input("Enter the String ")
str2=[]
for i in str1:
    if i not in str2:
        str2.append(i)
          
print(str2)"""


#using dictionary
str1=input("Enter the string: ")
str2="".join(dict.fromkeys(str1))
print(str2)