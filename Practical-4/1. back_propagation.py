import pandas as pd
import numpy as np

print("Name: Harsh Save")
X=np.array(([2,9],[1,5],[3,6]),dtype=float)
Y=np.array(([92],[86],[89]),dtype=float)
X=X/np.amax(X,axis=0)
Y=Y/100

class NM:
    def __init__(self):
        self.inputsize=2
        self.outputsize=1
        self.hiddensize=3
        
        self.W1=np.random.randn(self.inputsize,self.hiddensize)
        self.W2=np.random.randn(self.hiddensize,self.outputsize)
    
    def forward(self,X):
        self.z=np.dot(X,self.W1)
        self.z2=self.sigmoid(self.z)
        self.z3=np.dot(self.z2,self.W2)
        op=self.sigmoid(self.z3)
        return op
    
    def sigmoid(self,s):
        return 1/(1+np.exp(-s))


obj=NM()
op=obj.forward(X)
print("Actual output: ",str(op))
print("Expected output: ",str(Y))