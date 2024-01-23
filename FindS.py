import numpy as np
import pandas as pd
df=pd.read_csv("/content/enjoysport.csv")
print(df)
a=np.array(df)[: , :-1]
print(f"attributes are: {a}")
t=np.array(df)[:,-1]
print(f"Targets are {t}")
def train(a,t):
  for i,val in enumerate(t):
    if val=="yes":
      specific_hypothesis=a[i]
    break
  for i,val in enumerate(a):
    if t[i]=="yes":
       for x in range(0,len(specific_hypothesis)):
        if val[x]!=specific_hypothesis[x]:
          specific_hypothesis[x]="?"
        else:
          pass
  return specific_hypothesis
print(f"The final hypothesis is {train(a,t)}")
