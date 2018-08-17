'''Count even and odd numbers in that list.'''
list1=[]
n=int(input("Enter number of items you want in the list "))
for i in range(0,n):
    item=int(input("Enter item "))
    list1.append(item)
print(list1)

counteven=0
for i in range(n):
    if(list1[i]%2==0):
        counteven+=1

print("Count of even numbers= ",counteven)
print("Count of odd numbers= ",n-counteven)
