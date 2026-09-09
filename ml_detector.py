import joblib


# Load the trained model
model = joblib.load("scam_model.pkl")

# Load the TF-IDF vectorizer
vectorizer = joblib.load("tfidf_vectorizer.pkl")


def predict_scam(message):

    # Convert message into TF-IDF features
    message_tfidf = vectorizer.transform([message])

    # Make prediction
    prediction = model.predict(message_tfidf)[0]

    # Get scam probability
    probability = model.predict_proba(message_tfidf)[0][1]

    # Convert prediction to text
    if prediction == 1:
        result = "SCAM"
    else:
        result = "LEGITIMATE"

    return result, probability