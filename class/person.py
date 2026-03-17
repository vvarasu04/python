class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=str(age)
    def greet(self):
        print("Hello, my friend is " + self.name)
        print("His age is "+ self.age)
p1=Person("Emil",25)
p2=Person("Venketesh",27)
p3=Person("Pandy",27)
p4=Person("Prem",28)
p1.greet()
p2.greet()
p3.greet()
p4.greet()