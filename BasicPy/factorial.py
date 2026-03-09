"""num=int(input("Enter the number to find factorial: "))
def factorial(num):
    if(num==0):
        return 1
    return num*factorial(num-1)
print(factorial(num))"""

#using forloop

num=int(input("Enter the Number to Find: "))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)


