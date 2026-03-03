"""rows=5
for i in range(1,rows+1):
    print(' '*(rows-i)+'* '* i) """
          
          
          
rows=5

for i in range(1,rows+1):
    for j in range(5):
        if j%2==0:
            print("0",end=" ")
        else:
            print("1",end=" ")
            
    print()