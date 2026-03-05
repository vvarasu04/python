#simple method
"""string = input("Enter the String: ")
reverse = string[::-1]
print("Reverse value is:",reverse) """

#using forloop

"""word = input("Enter the word:")
reversed_word = ""
for i in range (len(word)-1,-1,-1):
    reversed_word+=word[i]
print("reversed word is:",reversed_word)"""



"""str1=input("Enetr the string to reverse: ")
str2=""
for i in str1:
    str2=i+str2
print(str2)"""

#palindrome check

str1=input("Enter the string to check: ")
str2=''
for i in str1:
    str2=i+str2
if(str1==str2):
    print("palindrome")
else:
    print("Not a palindrome")
    