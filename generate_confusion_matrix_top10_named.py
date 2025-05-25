
import pandas as pd
from joblib import load
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, MultiLabelBinarizer
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


df = pd.read_csv("animal_disease_dataset_extended.csv")


features = ['Animal', 'Age', 'Temperature', 'Symptom 1', 'Symptom 2', 'Symptom 3']
target = 'Disease'
df_clean = df.dropna(subset=features + [target])


le_animal = load("model/le_animal_update.pkl")
le_disease = load("model/le_disease.pkl")
mlb = load("model/mlb_symptoms.pkl")
model = load("model/animal_disease_model_compressed.joblib")


df_clean['Animal'] = le_animal.transform(df_clean['Animal'])
df_clean['Disease'] = le_disease.transform(df_clean['Disease'])
df_clean['All_Symptoms'] = df_clean[['Symptom 1', 'Symptom 2', 'Symptom 3']].values.tolist()
df_clean['All_Symptoms'] = df_clean['All_Symptoms'].apply(lambda x: list(set(filter(pd.notna, x))))
symptom_encoded = mlb.transform(df_clean['All_Symptoms'])


X = pd.concat([
    df_clean[['Animal', 'Age', 'Temperature']].reset_index(drop=True),
    pd.DataFrame(symptom_encoded, columns=mlb.classes_)
], axis=1)
y = df_clean['Disease']

_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
y_pred = model.predict(X_test)


top_classes = pd.Series(y_test).value_counts().head(10).index.tolist()
mask = y_test.isin(top_classes)
y_test_top = y_test[mask]
y_pred_top = pd.Series(y_pred, index=y_test.index)[mask]

# Confusion Matrix 
cm = confusion_matrix(y_test_top, y_pred_top, labels=top_classes)
labels_named = le_disease.inverse_transform(top_classes)

fig, ax = plt.subplots(figsize=(10, 8))
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels_named)
disp.plot(ax=ax, xticks_rotation=45)
plt.title("Confusion Matrix - Predicted Diseases")
plt.tight_layout()
plt.savefig("confusion_matrix_top10_named.png", dpi=150)
plt.show()
