num=input("Enter the Number: ")
original_num=num
sum=0

while num > 0:
    digit=num%10
    sum+=digit**3
    num=num//10
    
if sum==original_num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")