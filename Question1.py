'''Create a list with user defined inputs.'''
list1=[]
n=int(input("Enter number of items you want in the list "))
for i in range(0,n):
    item=int(input("Enter item "))
    list1.append(item)
print(list1)
