import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

data = {
    "hours_studied": [1, 2, 3, 4, 5, 6],
    "hours_slept": [7, 6, 5, 4, 3, 2],
    "grade": ["low", "low", "medium", "medium", "high", "high"]
}

df = pd.DataFrame(data)

le = LabelEncoder()
X = df[["hours_studied","hours_slept"]]
y = le.fit_transform(df["grade"])
X_train, X_test , y_train , y_test = train_test_split(X,y,test_size = 0.2 , random_state = 0)

model = LogisticRegression(multi_class="multinomial", solver="lbfgs")

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print (df)
print (y)
print (X_test)
print(y_pred)


