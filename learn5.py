from fastapi import FastAPI
#path and query perameters
app =FastAPI()

#query p.
all_customers = [
    {"id":101, "name":"Ravi", "city": "bengaluru", "risk":"low"}, 
    {"id":102, "name":"Om", "city":"mumbai", "risk":"high"}, 
    {"id":103, "name": "Prakash", "city": "mumbai", "risk":"high"}, 
    {"id":104, "name": "Yash", "city": "bengaluru", "risk":"high"}, 
    {"id":105, "name": "Gopal;", "city": "bengaluru", "risk":"high"},
]

@app.get("/customer")
def customer_get(city:str,risk:str):
    filtered = [
        c for c in all_customers
        if c["city"]==city and c["risk"]==risk
    ]
    return {
        "city":city,
        "risk":risk,
        "count":len(filtered),
        "results":filtered
    }


#path p.
customer={
    101:{
        "nsme":"ravi","risk":"high","score":1022
    },
    102:{
        "nsme":"madhu","risk":"low","score":2108
    },
    103:{
        "nsme":"karan","risk":"high","score":3297
    }
}
@app.get("/customer/{customer_id}")
def customer_get(customer_id:int):
    if customer_id not in customer:
        return {
            "Error":"Customer not found"
        }
    else :
        return customer[customer_id]


@app.get("/model/{model_name}/customer/{customer_id}")
def get_model_prediction (model_name: str, customer_id:int):
    return {
        "Model" :model_name,
        "customer_id" : customer_id,
        "risk" : "high"
    }