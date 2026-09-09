import joblib


# Load trained model
model = joblib.load("scam_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")


# Get message from user
message = input("Enter a message: ")


# Convert message into TF-IDF
message_tfidf = vectorizer.transform([message])


# Predict
prediction = model.predict(message_tfidf)[0]

# Get probability
probability = model.predict_proba(message_tfidf)[0][1]


# Display result
if prediction == 1:
    print("\nPrediction: SCAM")
else:
    print("\nPrediction: LEGITIMATE")

print("Scam probability:", round(probability * 100, 2), "%")