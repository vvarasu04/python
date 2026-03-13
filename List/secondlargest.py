#second largest using (sort)
"""numbers=[10,2,33,56,87,43,96]
numbers.sort()
print(numbers[-2])"""

#using sort and set
"""numbers=[10,2,33,56,87,43,96,88,88]
numbers=list(set(numbers))
numbers.sort()
num=sorted(numbers)
print(numbers[-2])
print(numbers)
"""

#using loop

numbers=[10,2,33,56,87,43,96,88]
largest=second=float('-inf')
for num in numbers:
    if num>largest:
        second=largest
        largest=num
    elif num>second and num!=largest:
        num=second
print(second)
    