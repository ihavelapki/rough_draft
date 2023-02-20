from pydantic import BaseModel
from decimal import Decimal
from enum import Enum
from typing import Optional
from datetime import date


class OperationKind(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class User(BaseModel):
    id: int
    date: date
    kind: OperationKind
    amount: Decimal
    description: Optional[str]
