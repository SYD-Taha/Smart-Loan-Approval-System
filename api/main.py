# api/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load model pipeline
model = joblib.load('models\model.pkl')

app = FastAPI(
    title="Loan Approval Prediction API",
    description="An API that predicts loan approval based on applicant data",
    version="1.0"
)

# Define expected input fields
class LoanApplication(BaseModel):
    Gender: str
    Married: str
    Dependents: str
    Education: str
    Self_Employed: str
    ApplicantIncome: float
    CoapplicantIncome: float
    LoanAmount: float
    Loan_Amount_Term: float
    Credit_History: float
    Property_Area: str

@app.get("/")
def read_root():
    return {"msg": "Welcome to the Loan Approval Prediction API"}

@app.post("/predict")
def predict(application: LoanApplication):
    # Convert to dataframe
    input_df = pd.DataFrame([application.dict()])

    # Predict using loaded model pipeline
    prediction = model.predict(input_df)[0]
    result = "Approved ✅" if prediction == 1 else "Rejected ❌"

    return {
        "prediction": int(prediction),
        "result": result
    }
