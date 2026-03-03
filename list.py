"""cities=["chennai","madurai","coimbatore","trichy","salem"]
val=[3,5,6,3,2,9]
list1=["chennai",'salem',3,5]

print(cities[0])
print(val[2])
print(cities[:3])
print(cities[-2])
print(cities[::2])
print(val)

cities[3]="tiruchi"
print(cities)

#append
cities.append("Karur")
print(cities)



#insert
cities.insert(3,"Hosur")
print(cities)

#remove using del
del cities[3]
print(cities)

#remove using pop
deleted=cities.pop(1)
print(deleted)
print(cities) 
"""
#Remove by value
"""cities=["chennai","madurai","chennai","coimbatore","trichy","salem"]
city_del="chennai"
cities.remove(city_del)
print(cities)

#sorting to use assending order
print(sorted(cities)) #temporary sort

cities.sort()#permanent sort
print(cities)


#Reverse
cities.reverse()
print(cities)"""



print("Enter list of numbers . Enter Z to exit")
Alist=[]
while True:
    inp=input()
    if(inp=='z'):
        break
    Alist.append(inp)
print(Alist)
        
    