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

print("The numbers that are not in second list are: ")
for i in list1:
    if i not in list2:
        print(i)