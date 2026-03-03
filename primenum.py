n=int(input("enter a number"))
prime=""
def prime(n):
    for i in range(1,n+1):
        if(n%i==0):
            print("none prime")
print(prime(n))