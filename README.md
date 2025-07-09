# 🏦 Smart Loan Approval Prediction System

This project is a complete Machine Learning pipeline for predicting whether a loan application will be approved based on applicant details.

---

## 📌 Features

- ✅ Trained XGBoost model with full preprocessing
- 🚀 FastAPI backend for model predictions
- 💻 Streamlit frontend for user interaction
- 🧠 SHAP-based model explainability
- 🧰 Modular code with deployment readiness
- 📝 Well-structured and documented project

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/loan-approval-project.git
cd loan-approval-project
```

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Run FastAPI Backend

```bash
uvicorn api.main:app --reload
```

### 4. Run Streamlit Frontend

```bash
streamlit run frontend/app.py
```

---

## 🔍 Model Explainability

We used SHAP to explain model predictions and identify key features affecting loan approvals.  
Refer to: `notebooks/explainability.ipynb` for visualizations.

---

## 🧪 Sample API Request

```json
POST /predict

{
  "Gender": "Male",
  "Married": "Yes",
  "Dependents": "0",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 0,
  "LoanAmount": 150,
  "Loan_Amount_Term": 360.0,
  "Credit_History": 1.0,
  "Property_Area": "Urban"
}
```

### ✅ Response

```json
{
  "prediction": 1,
  "result": "Approved ✅"
}
```

---

## 📁 Project Structure

```
loan_approval_project/
├── api/                  # FastAPI backend
├── frontend/             # Streamlit frontend
├── models/               # Trained model and preprocessor
├── data/                 # Cleaned dataset
├── notebooks/            # EDA, training, explainability
├── requirements.txt
├── README.md
```

---

## 🧠 Tech Stack

- Python
- XGBoost
- scikit-learn
- FastAPI
- Streamlit
- SHAP

---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

- [Kaggle Loan Prediction Dataset](https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset)
- Open-source tools that made this possible 🎉
