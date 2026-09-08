from flask import Flask, render_template, request
from detector import analyze_message

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        message = request.form["message"]

        score, risk, reasons = analyze_message(message)

        return render_template(
            "index.html",
            score=score,
            risk=risk,
            reasons=reasons,
            message=message
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)