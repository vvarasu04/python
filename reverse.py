#simple method
"""string = input("Enter the String: ")
reverse = string[::-1]
print("Reverse value is:",reverse) """

#using forloop

word = input("Enter the word:")
reversed_word = ""
for i in range (len(word)-1,-1,-1):
    reversed_word+=word[i]
print("reversed word is:",reversed_word)