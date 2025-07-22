from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from utils.predict import make_prediction
from utils.ensemble import ensemble_predict

app = Flask(__name__)
CORS(app)  

@app.route("/ensemble-predict", methods=["POST"])
def ensemble():
    try:
        model_list = request.form.getlist("models")  # Multiple model names
        file = request.files.get("file")

        if not model_list or not file:
            return jsonify({"error": "Missing model list or file"}), 400

        df = pd.read_csv(file)
        result = ensemble_predict(model_list, df)

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/")
def home():
    return "Maternal Health AI Backend is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        model_name = request.form.get("model")
        file = request.files.get("file")

        if not model_name or not file:
            return jsonify({"error": "Missing model or file"}), 400

        df = pd.read_csv(file)
        result = make_prediction(model_name, df)

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
