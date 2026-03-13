sentence=input("Enter the Sentence: ")
words=sentence.split(" ")
longest=""
for i in range(len(sentence)):
    substr=''
    for j in range(i,len(sentence)):
        if sentence[j] not in substr:
            substr=substr+sentence[j]
        else:
            break
if len(substr)>len(longest):
    longest=substr
print(longest)
            