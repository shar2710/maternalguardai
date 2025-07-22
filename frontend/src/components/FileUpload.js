import React, { useState } from "react";
import axios from "axios";

export default function FileUpload({ model, setPredictions }) {
  const [file, setFile] = useState(null);

  const handleUpload = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("model", model);
    formData.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:5000/predict", formData);
      setPredictions(res.data.predictions);
    } catch (err) {
      alert("Error: " + err.response?.data?.error || "Upload failed");
    }
  };

  return (
    <div>
      <input type="file" accept=".csv" onChange={(e) => setFile(e.target.files[0])} />
      <button onClick={handleUpload}>Upload & Predict</button>
    </div>
  );
}
