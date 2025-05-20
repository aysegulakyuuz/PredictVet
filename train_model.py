import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer

df = pd.read_csv("animal_disease_dataset_extended.csv")

le_animal = LabelEncoder()
df['animal_encoded'] = le_animal.fit_transform(df['Animal'])

le_disease = LabelEncoder()
df['disease_encoded'] = le_disease.fit_transform(df['Disease'])

symptom_cols = ['Symptom 1', 'Symptom 2', 'Symptom 3']
df['all_symptoms'] = df[symptom_cols].values.tolist()
mlb = MultiLabelBinarizer()
symptom_features = mlb.fit_transform(df['all_symptoms'])

X = np.hstack([df[['animal_encoded', 'Age', 'Temperature']].values, symptom_features])
y = df['disease_encoded'].values

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)

import os
os.makedirs("model", exist_ok=True)
pickle.dump(clf, open("model/animal_disease_model.pkl", "wb"))
pickle.dump(le_animal, open("model/le_animal.pkl", "wb"))
pickle.dump(le_disease, open("model/le_disease.pkl", "wb"))
pickle.dump(mlb, open("model/mlb_symptoms.pkl", "wb"))

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


clf_test = RandomForestClassifier(n_estimators=100, random_state=42)
clf_test.fit(X_train, y_train)


y_pred = clf_test.predict(X_test)


print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
