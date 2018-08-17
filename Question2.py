''' Add the following list to above created list: 
[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]  '''

list1=[]
n=int(input("Enter number of items you want in the list "))
for i in range(0,n):
    item=int(input("Enter item "))
    list1.append(item)
print(list1)

list2=['google','apple','facebook','microsoft','tesla']
list1.extend(list2)
print(list1)
