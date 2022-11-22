print("Name: Harsh Save")
w1=[0,0,0,0]
w2=[0,0,0,0]

for m in range(0,4):
    print("Enter 4 binary input values")
    s=[]
    t=[]
    
    for i in range(0,4):
        x=int(input())
        s.append(x)
    print("Enter 2 binary target values")
    for i in range(0,2):
        x=int(input())
        t.append(x)
    
    print("s= ",s)
    print("t= ",t)

    w1New=[]
    for i in range(0,4):
        newWeight=w1[i]+s[i]*t[0]
        w1New.append(newWeight)
    
    for i in range(0,4):
        print("W",(i+1),"1= ",w1New[i])
    
    
    w2New=[]
    for i in range(0,4):
        newWeight=w2[i]+s[i]*t[1]
        w2New.append(newWeight)
    
    for i in range(0,4):
        print("W",(i+1),"2= ",w2New[i])
    
    w1=w1New
    w2=w2New
    
    print(w1)
    print(w2)
    
print("The final weight matrix is ")
print("W= ")
for i in range(0,4):
    print(w1[i],w2[i])
print("Done")
    