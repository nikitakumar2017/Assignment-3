'''Print true if the string contains all numeric characters. '''
str1=input("Enter string")
l=len(str1)
flag=0
i=0
while (i<l and flag==0):
    if(str1[i].isdigit()==True):
        flag=0
    else:
        flag=1
    i=i+1
if(i==l):
    if(flag==0):
        print("True")
else:
    print("False")
    
