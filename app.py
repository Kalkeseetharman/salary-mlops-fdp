
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import mlflow
import logging

# Configure logging
logging.basicConfig(
    filename="salary_api.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    force=True
)

# Load MLflow model
model = mlflow.pyfunc.load_model("models:/SalaryPredictionModel/2")

app = FastAPI(title="Salary Prediction API")

class Employee(BaseModel):
    Age: int
    Gender: str
    Education_Level: str
    Job_Title: str
    Years_of_Experience: float

@app.get("/health")
def health():
    logging.info("Health endpoint accessed")
    return {
        "status": "Running",
        "model": "SalaryPredictionModel Version 2"
    }

@app.post("/predict")
def predict(employee: Employee):

    try:

        input_df = pd.DataFrame([{
            "Age": employee.Age,
            "Gender": employee.Gender,
            "Education Level": employee.Education_Level,
            "Job Title": employee.Job_Title,
            "Years of Experience": employee.Years_of_Experience
        }])

        prediction = model.predict(input_df)

        logging.info(f"Prediction : {prediction[0]}")

        return {
            "Predicted Salary": round(float(prediction[0]), 2)
        }

    except Exception as e:

        logging.error(str(e))

        return {"Error": str(e)}
