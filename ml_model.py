import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
df = pd.read_csv("Dataset.csv")

# Encode labels (positive = 1, negative = 0)
le = LabelEncoder()
df["status"] = le.fit_transform(df["status"])

# Features and target
X = df.drop("status", axis=1)
y = df["status"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save model and label encoder
joblib.dump(model, "health_model.pkl")
joblib.dump(le, "label_encoder.pkl")

print("✅ Model trained and saved successfully!")
