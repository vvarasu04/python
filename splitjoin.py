#split delimit by comma(,) also use whitespace
"""text='aaa,bbb,ccc,ddd'
newtext=text.split(',')
print(newtext)"""

text="agr yrt yat"
newtext=text.split(" ")
print(newtext)

#join using  hypen- comma, space 
joined='-'.join(newtext)
print(joined)