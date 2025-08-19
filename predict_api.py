from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("model.joblib")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = [[data["age"], data["diabetes"], data["hypertension"], data["length_of_stay"]]]
    risk = model.predict_proba(features)[0][1]
    return jsonify({"readmission_risk": round(risk, 3)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
