from pydantic import BaseModel
from typing import List


class Order(BaseModel):
    components: List[str]


class OrderResponse(BaseModel):
    order_id: str
    total: float
    parts: List[str]
