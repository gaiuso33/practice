#preprocess
import time
import nltk
import re
import pandas as pd
import time
import os
import joblib
import sys
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, precision_score
from sklearn.preprocessing import LabelEncoder
from preprocess import preprocess_text
from sklearn.metrics.pairwise import cosine_similarity

sys.stdout.reconfigure(encoding='utf-8')
start_time = time.time()
# Download NLTK dependencies
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
#function to preprocess text
def preprocess_text(text):
    text = text.lower()
    text = text.encode("ascii", "ignore").decode() 
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word not in stop_words]
    return " ".join(words)
# Load dataset
df = pd.read_csv(r"C:\Users\Ayogaius\Desktop\result-screening-system\data\resume_dataset.csv", encoding="utf-8")
# Apply function to dataset
df["Cleaned_Resume"] = df["Resume"].apply(preprocess_text)

# Show processed data
print("Sample stopwords:", list(stop_words)[:5])  # Check stopwords
print("Lemmatization example:", lemmatizer.lemmatize("running"))  # Check lemmatization
print(df["Cleaned_Resume"].head())
df.to_csv(r"C:\Users\Ayogaius\Desktop\result-screening-system\data\processed_resume_dataset.csv", index=False)
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Processing Time: {elapsed_time:.2f} seconds")

#train-model

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


#rank-candidates


start_time = time.time()
# Get base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Define paths for models and processed dataset
DATA_PATH = os.path.join(BASE_DIR, "../data/processed_resume_dataset.csv")
MODEL_PATH = os.path.join(BASE_DIR, "../models/tfidf_vectorizer.pkl")
CLASSIFIER_PATH = os.path.join(BASE_DIR, "../models/resume_classifier.pkl")
# Load trained model & vectorizer
vectorizer = joblib.load(MODEL_PATH)
model = joblib.load(CLASSIFIER_PATH)
# Load dataset
df = pd.read_csv(DATA_PATH, encoding="utf-8")
df["Cleaned_Resume"] = df["Resume"].apply(preprocess_text)
X = vectorizer.transform(df["Cleaned_Resume"])
# Job Description Input
job_description = """Data Science"""
job_vector = vectorizer.transform([preprocess_text(job_description)])
# Compute similarity
similarity_scores = cosine_similarity(job_vector, X)
# Add scores to dataset
df["Similarity_Score"] = similarity_scores[0]
# Sort candidates in an ascending order
ranked_resumes = df.sort_values(by="Similarity_Score", ascending=False)
ranked_resumes = ranked_resumes.sort_values(by="Similarity_Score", ascending=False)
ranked_resumes["Resume"] = ranked_resumes["Resume"].str.replace(r"\r\n", " ", regex=True)
# list top matches
print(ranked_resumes[["Resume", "Similarity_Score"]].head(10))
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Processing Time: {elapsed_time:.2f} seconds")