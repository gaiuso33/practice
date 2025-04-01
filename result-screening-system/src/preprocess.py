import time
import nltk
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
start_time = time.time()
# Download NLTK dependencies
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = text.lower()
    text = text.encode("ascii", "ignore").decode()  # Remove special characters
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