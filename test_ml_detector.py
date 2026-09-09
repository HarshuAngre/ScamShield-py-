from ml_detector import predict_scam


message = input("Enter a message: ")

result, probability = predict_scam(message)

print("\nPrediction:", result)
print("Scam probability:", round(probability * 100, 2), "%")