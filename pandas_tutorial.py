import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s=pd.Series([1,3,5,4,5])
s

a=np.array([1,2,3,4,8])
a

s=pd.Series(a,name="A")
s

df=pd.DataFrame(np.random.randint(0,10,size=(5,4)),columns=["A","B","C","D"])
df

df["E"]=s
df

q=pd.read_csv("prova.csv")
q

c=q["Visit"]
print(q["Visit"])

