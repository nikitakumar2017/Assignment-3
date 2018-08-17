''' create a list with numbers and sort it in ascending order. '''
list1=[]
n=int(input("Enter number of items you want in the list "))
for i in range(0,n):
    item=int(input("Enter item "))
    list1.append(item)
print("The original list is: ",list1)
list1.sort()
print("The sorted list is: ",list1)
