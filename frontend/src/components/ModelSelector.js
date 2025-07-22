import React from "react";

export default function ModelSelector({ model, setModel }) {
  return (
    <div>
      <label>Select Model:</label>
      <select value={model} onChange={(e) => setModel(e.target.value)}>
        <option value="LogisticRegression">Logistic Regression</option>
        <option value="RandomForest">Random Forest</option>
        <option value="SVM">SVM</option>
        <option value="XGBoost">XGBoost</option>
      </select>
    </div>
  );
}
