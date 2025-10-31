from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

data = {
    "hours_studied": [1, 2, 3, 4, 5, 6],
    "hours_slept": [7, 6, 5, 4, 3, 2],
    "grade": ["low", "low", "medium", "medium", "high", "high"]
}


import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression

df = pd.DataFrame(data)

X = df[["hours_studied","hours_slept"]]
y = df["grade"]

le = LabelEncoder()

y = le.fit_transform(y)

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2, random_state=0)

model = LogisticRegression()

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print(y_pred)