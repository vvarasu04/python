"""n=int(input("Enter the number to find: "))
def factorial(n):
    if(n==0):
        return 1
    return n*factorial(n-1)
print(factorial(n))"""
n=5
def fact(n):

        if(n==0):
            return 1
        return n*fact(n-1)
print(fact(n))