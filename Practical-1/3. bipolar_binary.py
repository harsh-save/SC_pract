import math
print("Name: Harsh Save")
n=int(input("Enter number of input "))
Yin=0
for _ in range(n):
    x=float(input("Enter x "))
    w=float(input("Enter w "))
    b=float(input("Enter b "))
    Yin=(Yin+(w*b)+b)
print("Yin ",Yin)

binary_sigmoid=(1/(1+(math.e**(-Yin))))
bipolar_sigmoid=(2/(1+(math.e**(-Yin))))+1
print("Binary Sigmoid ",round(binary_sigmoid,3))
print("Bipolar Sigmoid ",round(bipolar_sigmoid,3))