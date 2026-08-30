from fastapi import FastAPI

app = FastAPI()


@app.get("/customer")
def get_customer_id(c_id: int):
    return {
    "customer_id":c_id,
    "name":"Jiyansh",
    "status":"Active"
}