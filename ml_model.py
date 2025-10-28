import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# === 1. Charger le dataset ===
df = pd.read_csv("data2.csv")

# === 2. Préparer la cible ===
df["status"] = df["status"].map({"positive": 1, "negative": 0})

# === 3. Définir X et y ===
X = df.drop(columns=["status"])
y = df["status"]

# === 4. Séparer train/test ===
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# === 5. Créer un pipeline ===
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42
    ))
])

# === 6. Entraîner le modèle ===
pipeline.fit(X_train, y_train)

# === 7. Évaluer la performance ===
y_pred = pipeline.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("🎯 Accuracy :", round(accuracy * 100, 2), "%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# === 8. Sauvegarder le modèle ===
joblib.dump(pipeline, "model.joblib")
print("✅ Modèle sauvegardé sous model.joblib")
