#number triangle
"""rows =5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print(" ")
    """
    
#same number in a row

"""rows=5
for i in range(1,rows+1):
    for j in range(0,i):
        print(i, end=" ")
    print("")"""
    
#Floyd's triangle
"""rows=5
num=1
for i in range(1,rows+1):
    for j in range(i):
        print(num, end=" ")
        num+=1
    print("")"""
    
    
#reverse number triangle
rows=5
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print("")