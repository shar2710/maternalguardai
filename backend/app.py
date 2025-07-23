from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from utils.predict import make_prediction
from utils.ensemble import ensemble_predict

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Maternal Health AI Backend is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        model_name = data.get("model")
        input_data = data.get("features")

        if not model_name or not input_data:
            return jsonify({"error": "Missing model or input data"}), 400

        df = pd.DataFrame([input_data]) 
        result = make_prediction(model_name, df)

        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/ensemble-predict", methods=["POST"])
def ensemble():
    try:
        model_list = request.form.getlist("models")  # Expect multiple 'models' keys
        file = request.files.get("file")

        if not model_list or not file:
            return jsonify({"error": "Missing 'models' or 'file' in form-data"}), 400

        try:
            df = pd.read_csv(file)
        except Exception as e:
            return jsonify({"error": f"Failed to read uploaded file: {str(e)}"}), 400

        result = ensemble_predict(model_list, df)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
