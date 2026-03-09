#using recursion
"""n=int(input("Enter the Number: "))
def fib(n):
    if(n<=1):
        return 1
    else:
        return fib(n-1)+fib(n-2)
print("")

for i in range(n):
    print(fib(i))"""
    
#using for loop
n=int(input("Enter the Number: "))
a=0
b=1



for i in range(n):
    print(a,end=' ')
    c=a+b
    a=b
    b=c

    