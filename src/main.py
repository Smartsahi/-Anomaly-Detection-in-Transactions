import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load the dataset
data = pd.read_csv('dataset/transaction_anomalies_dataset.csv')

# Data Preprocessing
data['Is_FRAUD'] = 0  # Placeholder column for fraud labels

# Select features
features = ['Transaction_Amount', 'Average_Transaction_Amount', 'Frequency_of_Transactions']
X = data[features]

# Split data
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Train the Isolation Forest model
model = IsolationForest(contamination=0.02, random_state=42)
model.fit(X_train)

# Predict
y_pred = model.predict(X_test)

# Convert predictions to binary (1: fraud, 0: normal)
y_pred = [1 if x == -1 else 0 for x in y_pred]

# Evaluation
print("Model Evaluation:\n")
print(classification_report([0] * len(y_pred), y_pred))
