list1=[]
print("Enter 5 numbers")
for i in range(0,5):
    v=input()
    list1.append(v)
    

list2=[]
print("Enter 5 numbers")
for i in range(0,5):
    v=input()
    list2.append(v)


flag=0
for i in list1:
    if i in list2:
        flag=1
if flag==1:
    print("The lists overlap")
else:
    print("The lists do not overlap")