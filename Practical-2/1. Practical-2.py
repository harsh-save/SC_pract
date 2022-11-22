print("Name: Harsh Save")
print("XOR function using Mc-Culloch Pitts neuron")


x1inputs=[]
x2inputs=[]

c=input("Enter 1 to input values or press enter to use default values ")
if c=='1':
    for _ in range(0,4):
        x1=int(input("Enter x1"))
        x1inputs.append(x1)
        x2=int(input("Enter x2"))
        x2inputs.append(x2)
else:
    x1inputs=[1,1,0,0]
    x2inputs=[1,0,1,0]


print("Considering one weight are excitatory and the other inhibitory")
w1=[1,1,1,1]
w2=[-1,-1,-1,-1]
z1=[]

for i in range(0,4):
    z1.append(x1inputs[i]*w1[i]+x2inputs[i]*w2[i])

print("X1","X2","Z1")
for i in range(0,4):
    print(x1inputs[i]," ",x2inputs[i]," ",z1[i])

print("Considering one weight are excitatory and the other inhibitory")
w2=[1,1,1,1]
w1=[-1,-1,-1,-1]
z2=[]

for i in range(0,4):
    z2.append(x1inputs[i]*w1[i]+x2inputs[i]*w2[i])

print("X1","X2","Z2")
for i in range(0,4):
    print(x1inputs[i]," ",x2inputs[i]," ",z2[i])


print("Applying Threshold")

for i in range(0,4):
    if z1[i]>=1:
        z1[i]=1
    else:
        z1[i]=0
    if z2[i]>=1:
        z2[i]=1
    else:
        z2[i]=0

print("z1"," ","z2")
for i in range(0,4):
    print(z1[i]," ",z2[i])

Y=[]
v1=1
v2=1

for i in range(0,4):
    Y.append(z1[i]*v1+z2[i]*v2)

print("Z1"," ","z2"," ","Y")
for i in range(0,4):
    print(z1[i]," ",z2[i]," ",Y[i])
