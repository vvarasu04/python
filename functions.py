#farehenit to celsious function
"""fahrenheit=int(input("Enter the temperature:"))

def fahrenheit_to_celsious(fahrenheit):
    return (fahrenheit-32)*5/9

print(fahrenheit_to_celsious(fahrenheit))"""


def greet(name):
    print("Hi "+name)
    print("How are you")
name="veera"
greet(name)

#factorial function

def factorial(n):
    
        if(n==0):
            return 1
        return n*factorial(n-1)
    
print(factorial(5))


#sum of n numbers
n=int(input("Enter the number: "))
def sum(n):
    sumresult=(n*(n+1)/2)
    return sumresult
print(sum(n))

