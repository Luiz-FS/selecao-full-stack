from decimal import Decimal

from pydantic import BaseModel


class CoinSchema(BaseModel):
    name: str
    price: Decimal
