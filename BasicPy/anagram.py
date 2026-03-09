
def anagram(str1,str2):
    if(sorted(str1)==sorted(str2)):
        return True
    else:
        return False
    
str1=input("Enter the string: ")
str2=input("Enter the string: ")
if anagram(str1,str2):
    print("Anagram")
else:
    print("Non anagram")