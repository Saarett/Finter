from abc import ABC, abstractmethod
from typing import Tuple, Any

import pandas
from pandas import DataFrame

from src.TransactionData import TransactionData


class Extractor(ABC):
    __DATE = 'date'
    __COMPANY = 'company'
    __DESCRIPTION = 'description'
    __TRANSACTION_PRICE = 'transaction_price'
    __DEBIT_PRICE = 'debit_price'
    __REFERENCE = 'reference'
    __TRANSACTION_DATE = 'transaction_date'
    __TRANSACTION_TYPE = 'transaction_type'

    __date_ind = None
    __company_ind = None
    __description_ind = None
    __transaction_price_ind = None
    __debit_price_ind = None
    __reference_ind = None
    __transaction_date_ind = None
    __transaction_type_ind = None

    def __init__(self, date_ind, company_id, description_ind, transaction_price_ind, debit_price_ind, reference_ind, transaction_date_ind, transaction_type_ind):
        self.__date_ind = date_ind
        self.__company_ind = company_id
        self.__description_ind = description_ind
        self.__transaction_price_ind = transaction_price_ind
        self.__debit_price_ind = debit_price_ind
        self.__reference_ind = reference_ind
        self.__transaction_date_ind = transaction_date_ind
        self.__transaction_type_ind = transaction_type_ind

    def __generate_empty_data(self) -> object:
        return {
            self.__DATE: [],
            self.__COMPANY: [],
            self.__DESCRIPTION: [],
            self.__REFERENCE: [],
            self.__TRANSACTION_PRICE: [],
            self.__TRANSACTION_DATE: [],
            self.__TRANSACTION_TYPE: [],
            self.__DEBIT_PRICE: [],
        }

    def __insert_transaction_data(self, data_obj, transaction_data: TransactionData):
        data_obj[self.__DATE].append(transaction_data.date)
        data_obj[self.__COMPANY].append(transaction_data.company)
        data_obj[self.__DESCRIPTION].append(transaction_data.description)
        data_obj[self.__TRANSACTION_PRICE].append(transaction_data.transaction_price)
        data_obj[self.__TRANSACTION_DATE].append(transaction_data.transaction_date)
        data_obj[self.__TRANSACTION_TYPE].append(transaction_data.transaction_type)
        data_obj[self.__DEBIT_PRICE].append(transaction_data.debit_price)
        data_obj[self.__REFERENCE].append(transaction_data.reference)

    def extract_report(self, page: DataFrame) -> DataFrame:
        self._update_page_before_extract(page)
        report_data = self.__generate_empty_data()
        num_of_rows: int = page.shape[0]
        for idx, r in enumerate(page.itertuples()):
            if self._should_break_report_iteration(idx, r, num_of_rows):
                break
            transaction_data: TransactionData = self.__extract_transaction_data(r)
            self.__insert_transaction_data(report_data, transaction_data)
        return DataFrame(data=report_data)

    def __extract_transaction_data(self, row: Tuple[Any, ...]) -> TransactionData:
        transaction_data = TransactionData()
        try:
            if self.__date_ind:
                transaction_data.date = row[self.__date_ind]
            if self.__company_ind:
                transaction_data.company = row[self.__company_ind]
            if self.__description_ind:
                transaction_data.description = row[self.__description_ind]
            if self.__transaction_price_ind:
                transaction_data.transaction_price = row[self.__transaction_price_ind]
            if self.__debit_price_ind:
                transaction_data.debit_price = row[self.__debit_price_ind]
            if self.__reference_ind:
                transaction_data.reference = row[self.__reference_ind]
            if self.__transaction_date_ind:
                transaction_data.transaction_date = row[self.__transaction_date_ind]
            if self.__transaction_type_ind:
                transaction_data.transaction_type = row[self.__transaction_type_ind]
        except:
            pass
        return transaction_data

    def _update_page_before_extract(self, page: DataFrame) -> None:
        pass

    def _should_break_report_iteration(self, idx: int, r: Tuple[Any, ...], num_of_rows: int) -> bool:
        return False
