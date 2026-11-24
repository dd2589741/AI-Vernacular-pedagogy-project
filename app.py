from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")


@app.route("/translate", methods=["POST"])
def translate():

    data = request.get_json()

    tamil_text = data.get("text", "").strip()

    if not tamil_text:

        return jsonify({
            "error": "Tamil text is required"
        }), 400

    # Model will be connected here in a later step.

    irula_text = "Model training and integration will be completed next."

    return jsonify({

        "translation": irula_text

    })


if __name__ == "__main__":

    app.run(debug=True)