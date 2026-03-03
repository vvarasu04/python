"""num=1
while  num<=100:
    print(num)
    num+=1"""
    

"""rows=5
num=1
for i in range(1,rows+1):
    print(" "*(rows-i)+ "* "*i)"""


"""for i in range(rows,0,-1):
    print(" "*(rows-i)+"* "*i)
print(" ")

for i in range(1,rows+1):
    for j in range(i):
        print(num,end=" ")
        num+=1
    print("")"""
        
        
#first line 00000 and second line 11111 pattern
"""for i in range(1,rows+1):
    for j in range(5):
        if(i%2==1):
            print("0", end=" ")
        else:
            print("1", end=" ")
    
    print(" ")"""
    
    
#01010 pattern
"""rows=5
for i in range(1,rows+1):
    for j in range(5):
       
            if (j%2==0):
                print("0",end="")
            else:
                print("1",end="")
        
    print("")"""
    
#first and last line 11111 center lines 10001 pattern

"""rows=5
for i in range(1,rows+1):
    for j in range(5):
        if(i==1):
            print("1", end=' ')
        elif(i==5):
            print("1",end=" ")
     
           
        elif(j==0):
            print("1",end=' ')
        elif(j==4):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print("")"""
    
    
#all the numbers are 11111 and center line of is 11011

rows=5
for i in range(1,rows+1):
    for j in range(5):
        if(i==3 and j==2):
            print("0", end=" ")
        else:
            print("1",end=" ")
    print("")
