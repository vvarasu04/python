#Program to Find the Longest Word in a Sentence using split
"""sent=input("Enter the sentence: ")
words=sent.split()
longest=''

for word in words:
    if len(word)>len(longest):
        longest=word
print(longest)"""
    
#Program to Find the Longest Word in a Sentence  without using split

"""sentence=input("Enter the sentence: ")
word=''
longest=''

for ch in sentence:
    if ch != " ":
        word=word+ch
    else:
        len(word)>len(longest)
        longest=word
        word=""
    if len(word)>len(longest):
        longest=word
print(longest)"""
    
sentence=input("Enter the sentence: ")
words=""
longest=''
for ch in sentence:
    if ch!=' ':
        words=words+ch
    else:
        len(words)>len(longest)
        longest=words
        words=''

    if len(words)>len(longest):
        longest=words
print(longest)
        