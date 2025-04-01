import time
import os
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, precision_score
from sklearn.preprocessing import LabelEncoder

start_time = time.time()
# Define paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
DATA_PATH = os.path.join(BASE_DIR, "../data/processed_resume_dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "../models/")
# Load preprocessed dataset
df = pd.read_csv(DATA_PATH, encoding="utf-8")
# Convert text to numerical features
vectorizer = TfidfVectorizer(max_features=5000)  # Increased features for better accuracy
X = vectorizer.fit_transform(df["Cleaned_Resume"])
# Encode categories
encoder = LabelEncoder()
y = encoder.fit_transform(df["Category"])
# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Train model
model = LogisticRegression()
model.fit(X_train, y_train)
# Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
print(f"Accuracy: {accuracy}, Precision: {precision}")
print(f" Model Accuracy: {accuracy:.2f}")
print("\n Classification Report:\n", classification_report(y_test, y_pred))
# Save the trained model & vectorizer
joblib.dump(model, os.path.join(MODEL_PATH, "resume_classifier.pkl"))
joblib.dump(vectorizer, os.path.join(MODEL_PATH, "tfidf_vectorizer.pkl"))
joblib.dump(encoder, os.path.join(MODEL_PATH, "category_encoder.pkl"))
print(" Model and vectorizer saved successfully!")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Processing Time: {elapsed_time:.2f} seconds")