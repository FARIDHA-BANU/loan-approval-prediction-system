import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load dataset
data = pd.read_csv('dataset/loan_approval_dataset.csv')

# Clean column names
data.columns = data.columns.str.strip()

# Clean loan_status values (remove spaces)
data['loan_status'] = data['loan_status'].astype(str).str.strip()

# Keep only rows with Approved or Rejected
data = data[data['loan_status'].isin(['Approved', 'Rejected'])]

# Features
X = data[['income_annum', 'loan_amount', 'loan_term', 'cibil_score']]

# Target
y = data['loan_status'].map({'Approved': 1, 'Rejected': 0})

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'model/loan_model.pkl')

print("Model trained successfully!")