from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
class loanapplication(BaseModel):
    age:int
    income:float
    loan_ammount:float
    employment_years:int
@app.post("/predict")
def post(application: loanapplication): 

    # pretend its an trend moodel..
    if application.income > 500000 and  application.employment_years>2:
        decition="Approved"
    else:
        decition="Rejected"

    return {
        "application_age":application.age,
        "decision":decition,
        "status":"active"
    }