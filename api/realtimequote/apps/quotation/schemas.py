from datetime import date
from decimal import Decimal

from pydantic import BaseModel


class QuotationSchema(BaseModel):
    min_price: Decimal
    max_price: Decimal
    variance: Decimal
    create_date: date
