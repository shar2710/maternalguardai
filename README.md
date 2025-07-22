# 🛡️ Maternal Guard AI

An AI-powered clinical decision support system for predicting **preeclampsia risk** in pregnant patients using real-world-inspired clinical data. Built with fairness, interpretability, and robustness in mind, it employs an **ensemble of machine learning models** (Random Forest, XGBoost, SVM) for superior accuracy.

![AUC Score](https://img.shields.io/badge/AUC-95.6%25-success?style=flat-square&logo=python&logoColor=white)

---

## 🚀 Features

- 🔬 Predicts **preeclampsia risk** from patient clinical data.
- 🧠 Utilizes **ensemble learning**: Random Forest + XGBoost + SVM.
- 📊 Built-in support for **SHAP explainability**.
- ⚖️ Handles class imbalance with **SMOTE**.
- 🏆 Achieved **95.6% AUC** on testing data.
- 🧪 RESTful API (FastAPI) – testable with Postman.
- 📓 Fully Jupyter-driven model training pipeline.

---

## 🗂️ Project Structure

```

MaternalGuardAI/
│
├── backend/
│   ├── app.py                    # FastAPI app entrypoint
│   ├── requirements.txt          # Python dependencies
│   ├── config/
│   │   └── config.py             # Constants and model paths
│   ├── models/
│   │   └── saved\_models/         # Trained model .pkl files
│   ├── notebooks/
│   │   ├── 01\_data\_exploration.ipynb
│   │   ├── 02\_feature\_engineering.ipynb
│   │   ├── 03\_model\_training.ipynb
│   │   ├── 04\_model\_evaluation.ipynb
│   │   └── 05\_ensemble\_model.ipynb
│   ├── utils/
│   │   ├── predict.py            # Model loading & prediction
│   │   ├── preprocessing.py      # Data preprocessing logic
│   │   └── ensemble.py           # Voting/averaging logic
│   └── data/
│       └── sample\_data.csv       # Sample input CSV
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── FileUpload.js
│   │   │   └── ModelSelector.js
│   │   └── api.js                # Axios configuration
│   └── package.json

````

---

## 📊 Clinical Parameters

| Feature                         | Description                              |
|---------------------------------|------------------------------------------|
| `blood_pressure_systolic`       | Systolic blood pressure                  |
| `urine_protein`                 | Protein in urine                         |
| `PlGF_level`, `sFlt1_PlGF_ratio`| Placental biomarkers                     |
| `gestational_age_weeks`         | Gestational age                          |
| `mean_arterial_pressure`        | Calculated BP indicator                  |
| `platelet_count`, `liver_enzymes`, `serum_creatinine` | Organ function labs         |
| `age`, `bmi`, `height_cm`, `weight_kg` | Demographic info                   |
| `preeclampsia` (label)          | Binary label (0/1) – **used in training**|

---

## 📈 Flowchart (End-to-End Inference)

```mermaid
flowchart TD
  A[Clinical Data Collection] --> B{Preprocessing}
  B --> C[Feature Engineering & Selection]
  C --> D[Model Inference]
  D --> E1[Random Forest Prediction]
  D --> E2[XGBoost Prediction]
  D --> E3[SVM Prediction]
  E1 --> F[Ensemble Voting/Stacking]
  E2 --> F
  E3 --> F
  F --> G[Risk Prediction Output]
  G --> H[SHAP Explainability]
  H --> I[Clinical Decision Support]

  style A fill:#b2dfdb,stroke:#1976d2,stroke-width:2px
  style G fill:#ffe082,stroke:#ffa000,stroke-width:2px
  style I fill:#81c784,stroke:#388e3c,stroke-width:2px
````

---

## ⚙️ Setup & Usage

### 1️⃣ Clone & Install Dependencies

```bash
git clone https://github.com/yourusername/maternalguardai.git
cd maternalguardai/backend
pip install -r requirements.txt
```

### 2️⃣ Train & Save Models (Jupyter Notebook)

Run `preitc.ipynb` (or notebooks 01–05) to:

* Preprocess data
* Train RF, SVM, XGBoost models
* Save `.pkl` files to `models/saved_models/`

### 3️⃣ Start Backend Server (FastAPI)

```bash
uvicorn app:app --reload
```

### 4️⃣ Test API with Postman

#### 🔍 Predict with One Model

**POST** `/predict`
**Form-Data:**

```
model: RandomForest
file: sample_data.csv
```

#### 🤝 Predict with Ensemble

**POST** `/ensemble-predict`
**Form-Data:**

```
file: sample_data.csv
```

---

## 📈 Model Performance

| Metric            | Score |
| ----------------- | ----- |
| AUC               | 95.6% |
| Balanced Accuracy | 92.3% |
| Precision         | 94.8% |
| Recall            | 96.2% |

---

## 🧠 Tech Stack

* 🔧 **FastAPI** – backend framework
* 🧪 **scikit-learn**, **XGBoost**, **SVM** – modeling
* 📊 **SHAP** – model explainability
* ⚖️ **SMOTE** – class imbalance handling
* 🌐 **Postman** – API testing
* 📓 **Jupyter** – model training notebooks

---

## 🔮 Future Roadmap

* 🏥 Integrate with real EMR/EHR datasets
* 🎤 Add voice-based symptom logging
* 📱 Deploy mobile app using Flutter
* 🧬 Integrate time-series LSTM models

---

## 💡 Inspiration

Preeclampsia remains a leading cause of maternal mortality. This project aims to build **interpretable, fair, and deployable AI tools** for clinicians to detect early warning signs and take proactive care decisions.

---

## 🙌 Contributions Welcome

If you'd like to contribute, feel free to fork the repo, open an issue, or submit a PR! 💙

---

## 📄 License

MIT License © [Sejal Sharma](https://github.com/yourusername)

```

---

