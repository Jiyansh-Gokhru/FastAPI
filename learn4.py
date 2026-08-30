#diffrence in get and post!
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

fake_database = {1: "Burger", 2: "Pizza" , 3: "Fries"}

@app.get("/get-item/{item_id}")
def read_item(item_id: int):
    return {"item": fake_database.get(item_id, "Item not found")}

orders_db = []

class Order(BaseModel):
    item_name: str
    quantity: int

@app.post("/place-order/")
def create_order(order: Order):
    orders_db.append(order)
    return {"message": "Order placed successfully!", "current_orders": orders_db}