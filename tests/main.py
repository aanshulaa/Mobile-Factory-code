from fastapi import FastAPI, HTTPException
from models import Order, OrderResponse
from order_service import create_order

app = FastAPI()


@app.post("/orders", response_model=OrderResponse, status_code=201)
def create_mobile_order(order: Order):
    try:
        order_details = create_order(order.components)
        return order_details
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
