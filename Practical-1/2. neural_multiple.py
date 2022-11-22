print("Name: Harsh Save")

n=int(input("Enter the number of inputs "))
Yin=0
for _ in range(n):
    weight=float(input("Enter the weight "))
    X=float(input("Enter the X "))
    Yin=Yin+weight*X
print("Yin= {}".format(Yin))
if Yin <0:
    out=0
elif Yin>1:
    out=1
else:
    out=Yin
print(out) 