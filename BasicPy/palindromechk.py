"""str1=input("enter the number to check Palindrome: ")
str2=''
for i in str1:
    str2=i+str2
if(str1==str2):
    print("It is a Palindrome")
else:
    print("Not a palindrome")"""

#using recursion
def palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrome(s[1:-1])

str1 = input("Enter string: ")

if palindrome(str1):
    print("Palindrome")
else:
    print("Not Palindrome")