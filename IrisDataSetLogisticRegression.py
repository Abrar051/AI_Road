import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split

from LogisticRegressionPractice import X_train, y_train

# Load the Iris dataset
iris = datasets.load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)

#df = pd.DataFrame(iris)

print (df.head())

df['species'] = iris.target
df['species'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

sns.pairplot(df, hue='species', diag_kind='kde')
plt.suptitle("Iris Dataset Feature Relationships", y=1.02)
plt.show()


X = iris.data
y = iris.target

print (X)
print (y)

X_train , X_test , y_train , y_test = train_test_split(X,y,test_size=0.2, random_state=0)

model = LogisticRegression(multi_class='multinomial',solver='lbfgs',max_iter=200)

model.fit(X_train , y_train)

y_pred = model.predict(X_test)

print(y_pred)
