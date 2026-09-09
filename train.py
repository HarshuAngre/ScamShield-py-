import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

import joblib


# Load dataset
data = pd.read_csv(
    "SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "message"]
)


# Convert labels
data["label"] = data["label"].map({
    "ham": 0,
    "spam": 1
})


# Separate messages and labels
X = data["message"]
y = data["label"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Convert text into numerical features
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english"
)

X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)


# Train ML model
model = LogisticRegression()

model.fit(X_train_tfidf, y_train)


# Test model
predictions = model.predict(X_test_tfidf)

accuracy = accuracy_score(y_test, predictions)

print("Model trained successfully!")
print("Accuracy:", round(accuracy * 100, 2), "%")


# Save model and vectorizer
joblib.dump(model, "scam_model.pkl")
joblib.dump(vectorizer, "tfidf_vectorizer.pkl")

print("Model saved as scam_model.pkl")
print("Vectorizer saved as tfidf_vectorizer.pkl")