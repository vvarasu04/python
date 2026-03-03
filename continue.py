#Remove , from a string using continue
"""str1='A,B,V,C,E,R'
str2=''
for i in str1:
    if i==',':
        continue
    str2=str2 + i
print(str2)"""

#using pass 
#pass is just a placeholder it do nothing

"""str1='A,B,V,C,E,R'
str2=''
for i in str1:
    if i==',':
        pass
    else:
        str2=str2+i
print(str2)"""

#str_ip=[3,4,5,2,8,9].given a string of numbers and comma,add the numbers delimited comma
str_ip='34,5,2,8,9'
numlist=[]
nextnum=True
str2=''
for i in str_ip:
    if nextnum:
        str2=''
        nextnum=False
    if i==',':
        numlist.append(int(str2))
        nextnum=True
        continue
    str2+=i
numlist.append(int(str2))
print(numlist)


str_i='34,5,2,8,9'
newlist=str_i.split(',')
print(newlist)
