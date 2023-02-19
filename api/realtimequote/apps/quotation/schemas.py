from pydantic import BaseModel
from decimal import Decimal
from datetime import date


class QuotationSchema(BaseModel):
    min_price: Decimal
    max_price: Decimal
    variance: Decimal
    create_date: date
