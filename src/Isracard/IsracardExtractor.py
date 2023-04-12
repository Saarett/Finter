from abc import ABC
from typing import Tuple, Any

from src.Extractor import Extractor


class IsracardExtractor(Extractor, ABC):
    def __init__(self, date_ind, company_id, description_ind, transaction_price_ind, debit_price_ind, reference_ind,
                 transaction_date_ind, transaction_type_ind):
        super().__init__(date_ind, company_id, description_ind, transaction_price_ind, debit_price_ind, reference_ind,
                         transaction_date_ind, transaction_type_ind)

    def _should_break_report_iteration(self, idx: int, r: Tuple[Any, ...], num_of_rows: int) -> bool:
        return idx == num_of_rows - 1
