import re


def analyze_message(message):

    score = 0
    reasons = []

    message = message.lower()

    # -----------------------------
    # 1. URGENCY DETECTION
    # -----------------------------

    urgent_words = [
        "urgent",
        "immediately",
        "act now",
        "hurry",
        "within 24 hours",
        "last chance",
        "limited time"
    ]

    for word in urgent_words:
        if word in message:
            score += 15
            reasons.append("Urgent language detected")
            break


    # -----------------------------
    # 2. PRIZE / LOTTERY SCAMS
    # -----------------------------

    prize_words = [
        "you won",
        "winner",
        "lottery",
        "prize",
        "congratulations",
        "lucky winner",
        "cash prize",
        "reward"
    ]

    for word in prize_words:
        if word in message:
            score += 20
            reasons.append("Prize or reward offer detected")
            break


    # -----------------------------
    # 3. SENSITIVE INFORMATION
    # -----------------------------

    security_words = [
        "otp",
        "password",
        "pin",
        "verification code",
        "cvv",
        "card number",
        "login details",
        "security code"
    ]

    for word in security_words:
        if word in message:
            score += 25
            reasons.append("Request for sensitive information detected")
            break


    # -----------------------------
    # 4. BANKING / KYC
    # -----------------------------

    banking_words = [
        "bank",
        "bank account",
        "kyc",
        "credit card",
        "debit card",
        "account blocked",
        "account suspended",
        "upi"
    ]

    for word in banking_words:
        if word in message:
            score += 20
            reasons.append("Banking or financial information detected")
            break


    # -----------------------------
    # 5. PAYMENT REQUEST
    # -----------------------------

    payment_words = [
        "pay",
        "payment",
        "send money",
        "transfer money",
        "make a payment",
        "pay now",
        "deposit"
    ]

    for word in payment_words:
        if word in message:
            score += 20
            reasons.append("Payment request detected")
            break


    # -----------------------------
    # 6. SUSPICIOUS LINKS
    # -----------------------------

    url_pattern = r"(https?://\S+|www\.\S+)"

    if re.search(url_pattern, message):
        score += 20
        reasons.append("Link detected")


    # -----------------------------
    # 7. PHONE NUMBER
    # -----------------------------

    phone_pattern = r"\b\d{10}\b"

    if re.search(phone_pattern, message):
        score += 10
        reasons.append("Phone number detected")


    # -----------------------------
    # LIMIT SCORE
    # -----------------------------

    score = min(score, 100)


    # -----------------------------
    # RISK LEVEL
    # -----------------------------

    if score >= 75:
        risk = "HIGH RISK"

    elif score >= 40:
        risk = "SUSPICIOUS"

    else:
        risk = "LOW RISK"


    return score, risk, reasons
if __name__ == "__main__":

    test_message = """
    URGENT! Congratulations! You won ₹50,000.
    Your bank account will be blocked.
    Click https://example.com and enter your OTP immediately.
    """

    score, risk, reasons = analyze_message(test_message)

    print("Score:", score)
    print("Risk:", risk)

    print("\nReasons:")

    for reason in reasons:
        print("-", reason)