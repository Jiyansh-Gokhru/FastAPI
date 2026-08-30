from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() 
class Loanapplicaton(BaseModel):
    name : str
    age : int
    income : float
    experience_year: int
    loan_ammount : float

@app.post("/predict")
def predict_post (application: Loanapplicaton):
    #model logic    
    approved = (
        application.income in range(1000,100000)  and
        application.age>18 and 
        application.experience_year>2 and 
        application.loan_ammount<100000000  
    )

    return {
        "applicant name" : application.name,
        "Status of approvel": "Approved" if approved else "Rejected"
    }