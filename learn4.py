#using get and post!
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

#get
db = {1: "Burger", 2: "Pizza" , 3: "Fries"}

@app.get("/get-item/{item_id}")
def read_item(item_id: int):
    return {"item": db.get(item_id, "Item not found")}

#post
MENU_PRICES = {
    "burger": 80,   
    "pizza": 150,
    "fries": 100
}


class FoodOrder(BaseModel):
    burger_qty: int = 0
    pizza_qty: int = 0
    fries_qty: int = 0

@app.post("/order-food/")
def calculate_bill(order: FoodOrder):
   
    burger_total = order.burger_qty * MENU_PRICES["burger"]
    pizza_total = order.pizza_qty * MENU_PRICES["pizza"]
    fries_total = order.fries_qty * MENU_PRICES["fries"]
    grand_total = burger_total + pizza_total + fries_total

    return {
        "status": "Order Placed Successfully!",
        "order_details": {
            "burger": f"{order.burger_qty} x ₹{MENU_PRICES['burger']} = ₹{burger_total}",
            "pizza": f"{order.pizza_qty} x ₹{MENU_PRICES['pizza']} = ₹{pizza_total}",
            "fries": f"{order.fries_qty} x ₹{MENU_PRICES['fries']} = ₹{fries_total}"
        },
        "total_bill": f"₹{grand_total}"
    }