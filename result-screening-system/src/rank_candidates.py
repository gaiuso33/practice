import time
import os
import pandas as pd
import joblib
from preprocess import preprocess_text
from sklearn.metrics.pairwise import cosine_similarity
import sys
sys.stdout.reconfigure(encoding='utf-8')

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