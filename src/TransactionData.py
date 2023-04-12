from dataclasses import dataclass
from typing import Optional


@dataclass
class TransactionData:
    """Class for keeping track of a transaction data."""
    date: Optional[str] = None
    company: Optional[str] = None
    description: Optional[str] = None
    transaction_price: Optional[str] = None
    transaction_date: Optional[str] = None
    transaction_type: Optional[str] = None
    debit_price: Optional[str] = None
    reference: Optional[str] = None

    def __init__(self):
        pass

    def with_date(self, date: str):
        self.date = date
        return self

    def with_company(self, company: str):
        self.company = company
        return self

    def with_description(self, description: str):
        self.description = description
        return self

    def with_transaction_price(self, transaction_price: str):
        self.transaction_price = transaction_price
        return self

    def with_transaction_date(self, transaction_date: str):
        self.transaction_date = transaction_date
        return self

    def with_transaction_type(self, transaction_type: str):
        self.transaction_type = transaction_type
        return self

    def with_debit_price(self, debit_price: str):
        self.debit_price = debit_price
        return self

    def with_reference(self, reference: str):
        self.reference = reference
        return self
