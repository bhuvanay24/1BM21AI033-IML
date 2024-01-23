import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn import tree

iris=pd.read_csv("/content/enjoysport.csv")
print(iris.info())
enc = preprocessing.OrdinalEncoder()
X=iris.iloc[:,:-1]
X=enc.fit_transform(X)
y=iris.iloc[: ,-1].array.reshape(-1,1)
y=enc.fit_transform(y)
decision=tree.DecisionTreeClassifier(criterion="entropy")
decision.fit(X,y)
decision.predict([[1,0,1,1,0,1]])