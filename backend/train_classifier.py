import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
import pickle

df = pd.read_csv('../backend/train_data/badminton_dataset.csv')

df = pd.get_dummies(df).astype(int)
df = df.drop(["Play_Badminton_No"], axis=1)

X = df.drop(["Play_Badminton_Yes"], axis=1)
y = df["Play_Badminton_Yes"]

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

dtree = tree.DecisionTreeClassifier()
dtree.fit(x_train, y_train)

# save the trained classifier
file_name = '../backend/trained_classifier_model/dt_model.sav'
pickle.dump(dtree, open(file_name, 'wb'))