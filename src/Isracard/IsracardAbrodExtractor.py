from abc import ABC

from src.Isracard.IsracardExtractor import IsracardExtractor


class IsracardAbroadExtractor(IsracardExtractor, ABC):
    __DEBIT_PRICE_IND = 1
    __TRANSACTION_PRICE_IND = 2
    __COMPANY_IND = 3
    __TRANSACTION_DATE_IND = 4
    __DATE_IND = 5
    __DESCRIPTION_IND = None
    __REFERENCE_IND = None
    __TRANSACTION_TYPE_IND = None

    def __init__(self):
        super().__init__(self.__DATE_IND, self.__COMPANY_IND, self.__DESCRIPTION_IND, self.__TRANSACTION_PRICE_IND,
                         self.__DEBIT_PRICE_IND, self.__REFERENCE_IND,
                         self.__TRANSACTION_DATE_IND, self.__TRANSACTION_TYPE_IND)

