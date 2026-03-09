#without using isalppha()
"""str1=input("Enter the String: ")
vowels="aeiouAEIOU"
v=0
c=0
for i in str1:
    if(i in vowels):
        v+=1
    else:
        c+=1
print(f"Consonants{c} and Vowels {v}")"""

#using Basic program using for loop

str1=input("Enter the String: ")

v=0
c=0
for ch in str1:
    if ch.lower() in "aeiou":
        v+=1
    elif ch.isalpha():
        c+=1
print("Vowels: ",v)
print("Consonants: ",c)

#using while loop
str1=input("Enter the String: ")
v=0
c=0
i=0
while i<len(str1):
    ch=str1[i]
    if ch.lower() in "aeiou":
        v+=1
    elif ch.isalpha():
        c+=1
    i+=1
print("Vowels: ",v)
print("Consonants: ",c)

