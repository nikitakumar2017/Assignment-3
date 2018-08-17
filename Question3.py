'''Count the number of time an object occurs in a list. '''
list1=[]
n=int(input("Enter number of items you want in the list "))
for i in range(0,n):
    item=int(input("Enter item "))
    list1.append(item)
print(list1)

num=int(input("Enter the number you want to find the count of"))
print(list1.count(num))
