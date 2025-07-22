from flask import Flask, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)
MODEL_DIR = "./models"

@app.route("/predict", methods=["POST"])
def predict():
    model_name = request.form.get("model")
    file = request.files.get("file")
    
    if not model_name or not file:
        return jsonify({"error": "Model name and CSV file are required."}), 400

    # Load data
    df = pd.read_csv(file)
    
    # Load model
    model_path = os.path.join(MODEL_DIR, f"{model_name}.pkl")
    if not os.path.exists(model_path):
        return jsonify({"error": "Model not found."}), 404

    model = joblib.load(model_path)
    predictions = model.predict(df)
    
    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
