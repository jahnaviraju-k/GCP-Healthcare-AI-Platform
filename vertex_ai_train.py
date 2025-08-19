from google.cloud import bigquery
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score
import pandas as pd
import joblib

# Load dataset from BigQuery
bq = bigquery.Client()
query = "SELECT age, diabetes, hypertension, length_of_stay, readmitted FROM `your_project.healthcare_dataset.patients`"
df = bq.query(query).to_dataframe()

X = df.drop("readmitted", axis=1)
y = df["readmitted"]

# Train model
model = GradientBoostingClassifier()
model.fit(X, y)

# Evaluate
roc = roc_auc_score(y, model.predict_proba(X)[:,1])
print("Training ROC-AUC:", roc)

# Save model
joblib.dump(model, "model.joblib")
