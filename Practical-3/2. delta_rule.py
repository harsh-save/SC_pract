import math

print("Name: Harsh Save")
x1=[0.3,0.5,0.8]
w1=[0.1,0.1,0.1]
t=1
a=0.1
diff=1
Yin=0
print("Using 3 inputs 3 weights 1 output.")
while(diff>0.4):
    for i in range(0,3):
        Yin=Yin+(x1[i]*w1[i])
    Yin=Yin+0.25
    Yin=round(Yin,3)
    print("Yin= ",Yin)
    print("Target= ",t)
    diff=t-Yin
    
    diff=round(diff,3)
    diff=math.fabs(diff)
    print("Error= ",diff)
    newW1=[]
    for i in range(0,3):
        W1new=w1[i]+a*diff*x1[i]
        W1new=round(W1new,2)
        newW1.append(W1new)
    print("New w1= ",newW1)
    w1=newW1
    
        