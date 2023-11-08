import pandas as pd
import re
data=pd.read_csv("friends.csv")
print(data.to_string())
name=data.iloc[:,0]
email=data.iloc[:,1]
for i in email:
    check=re.findall(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]",i)
    if check:
        print(f"{i}  is valid")
    else:
        print(f"{i} is invalid")
  