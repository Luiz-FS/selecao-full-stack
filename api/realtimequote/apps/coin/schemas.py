from pydantic import BaseModel
from decimal import Decimal


class CoinSchema(BaseModel):
    name: str
    price: Decimal
