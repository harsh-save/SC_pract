print("Name: Harsh Save")

X=float(input("Enter the input X "))
weight=float(input("Enter the input weight "))
bias=float(input("Enter the input bias "))
out=-1

Yin=(bias+(X*weight))
print("Y=X*weight+bias is {}".format(Yin))

if Yin <0:
    out=0
elif Yin>=0 and Yin<1:
    out=Yin
else:
    out=1
print(out)