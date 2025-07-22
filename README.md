# 🛡️ Maternal Guard AI

An AI-powered clinical decision support system to **predict preeclampsia** risks in pregnant patients using real-world clinical features. Designed with fairness, interpretability, and accuracy in mind, it uses **ensemble machine learning** (Random Forest, SVM, XGBoost) to ensure robust predictions.

![Preeclampsia Risk Prediction](https://img.shields.io/badge/AUC-95.6%25-success?style=flat-square\&logo=python\&logoColor=white)

---

## 🚀 Features

* 🔬 Predicts **preeclampsia risk** using clinical data.
* 🤖 **Ensemble model**: Combines predictions from Random Forest, XGBoost, and SVM.
* 📊 Feature importance using **SHAP** values (explainability).
* ⚖️ Handles **class imbalance** with techniques like SMOTE.
* ✅ Achieved **95.6% AUC** on testing data.
* 🌍 Built on **synthetic patient records** modeled after real-world parameters.
* 🧪 Exposed as a **RESTful API** (Testable in Postman).
* 🖥️ Jupyter-based training, FastAPI-based backend.

---

## 📁 Project Structure

```
maternalguardai/
├── backend/
│   ├── main.py                # FastAPI server with /predict and /ensemble-predict routes
│   ├── config/
│   │   └── model_config.py    # Paths to saved models
│   ├── models/
│   │   └── saved_models/      # Trained .pkl models (RandomForest, XGBoost, SVM, LogisticRegression)
├── notebooks/
│   └── preitc.ipynb           # Model training, evaluation, and saving
├── data/
│   └── sample_data.csv        # Sample patient record(s)
├── app.css                    # Styles (if applicable to frontend)
└── README.md
```

---

## 📊 Clinical Parameters Used

| Feature                                               | Description                            |
| ----------------------------------------------------- | -------------------------------------- |
| `blood_pressure_systolic`                             | Systolic blood pressure                |
| `urine_protein`                                       | Protein levels in urine                |
| `PlGF_level`, `sFlt1_PlGF_ratio`                      | Biomarkers linked to placental health  |
| `gestational_age_weeks`                               | Age of the pregnancy in weeks          |
| `mean_arterial_pressure`                              | Calculated from BP values              |
| `platelet_count`, `liver_enzymes`, `serum_creatinine` | Lab indicators for organ function      |
| `age`, `bmi`, `weight_kg`, `height_cm`                | Demographic data                       |
| `preeclampsia`                                        | Label (0 or 1) — only used in training |

---

## ⚙️ Setup Instructions

### 🔧 1. Clone and install dependencies

```bash
git clone https://github.com/yourusername/maternalguardai.git
cd maternalguardai/backend
pip install -r requirements.txt
```

### 📦 2. Train and Save Models

Inside Jupyter Notebook (`preitc.ipynb`):

* Run all cells to preprocess data, train models (RF, SVM, XGBoost), and export `.pkl` files to `models/saved_models`.

### ▶️ 3. Start Backend Server

```bash
uvicorn main:app --reload
```

### 🧪 4. Test via Postman

#### 📤 Predict with One Model

**POST** `/predict`
**Body (form-data):**

```
model: RandomForest
file: sample_data.csv (uploaded file)
```

#### 🧠 Predict with Ensemble

**POST** `/ensemble-predict`
**Body (form-data):**

```
file: sample_data.csv (uploaded file)
```

---

## 💡 Tech Stack

* **FastAPI** for REST API
* **Scikit-learn**, **XGBoost**, **SVM**
* **SHAP** for model explainability
* **SMOTE** for class balancing
* **Postman** for API testing
* **Jupyter Notebook** for training pipeline

---

## 📈 Results

* **Ensemble AUC**: `95.6%`
* **Balanced Accuracy**: `92.3%`
* **Precision**: `94.8%`
* **Recall (Sensitivity)**: `96.2%`

---

## 💬 Future Plans

* ✅ Integrate real-world EMR datasets (HIPAA compliant).
* 🎙️ Add voice-based symptom logging.
* 📱 Deploy to mobile using Flutter + Flask API.
* 🧠 Integrate time-series LSTM models for fetal monitoring.

---

## 🧠 Inspiration

Preeclampsia remains a leading cause of maternal mortality worldwide. **Maternal Guard AI** aims to assist clinicians with early detection using interpretable AI.

---

## 🙌 Contributions

Contributions welcome! Feel free to submit a PR or open an issue.

---

## 📄 License

MIT License © Sejal Sharma


