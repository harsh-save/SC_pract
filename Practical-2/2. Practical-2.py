print("Name: Harsh Save")
print("XOR function using Mc-Culloch Pitts neuron")

c=input("Enter 1 to input values or press enter to use default values")
x1inputs=[]
x2inputs=[]
if c=='1':
    for _ in range(0,4):
        x1=int(input("Enter x1"))
        x1inputs.append(x1)
        x2=int(input("Enter x2"))
        x2inputs.append(x2)
else:
    x1inputs=[1,1,0,0]
    x2inputs=[1,0,1,0]


print("Considering all weights are excitatory")

w1=[1,1,1,1]
w2=[1,1,1,1]
y=[]

for i in range(0,4):
    y.append(x1inputs[i]*w1[i]+x2inputs[i]*w2[i])

print("X1","X2","Y")
for i in range(0,4):
    print(x1inputs[i]," ",x2inputs[i]," ",y[i])


print("Considering one weight are excitatory and the other inhibitory")
w1=[1,1,1,1]
w2=[-1,-1,-1,-1]
y=[]

for i in range(0,4):
    y.append(x1inputs[i]*w1[i]+x2inputs[i]*w2[i])

print("X1","X2","Y")
for i in range(0,4):
    print(x1inputs[i]," ",x2inputs[i]," ",y[i])