import React from "react";
import FileUpload from "./components/FileUpload";
import ModelSelector from "./components/ModelSelector";
import "./App.css";

function App() {
  const [model, setModel] = React.useState("RandomForest");
  const [predictions, setPredictions] = React.useState([]);

  return (
    <div className="App">
      <h2>Maternal Health Prediction</h2>
      <ModelSelector model={model} setModel={setModel} />
      <FileUpload model={model} setPredictions={setPredictions} />
      <div>
        <h4>Predictions</h4>
        <ul>
          {predictions.map((p, i) => (
            <li key={i}>{p}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default App;
