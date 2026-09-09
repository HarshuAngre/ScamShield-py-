from flask import Flask, render_template, request
from detector import analyze_message
from ml_detector import predict_scam

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        message = request.form["message"]

        # Rule-based analysis
        score, risk, reasons = analyze_message(message)

        # ML analysis
        ml_result, ml_probability = predict_scam(message)

        if risk == "HIGH RISK":
            risk_class = "high"

        elif risk == "SUSPICIOUS":
            risk_class = "medium"

        else:
            risk_class = "low"

        return render_template(
            "index.html",
            score=score,
            risk=risk,
            risk_class=risk_class,
            reasons=reasons,
            ml_result=ml_result,
            ml_probability=ml_probability,
            message=message
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)