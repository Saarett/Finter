from abc import ABC

from pandas import DataFrame

from src.Extractor import Extractor


class LeumiCardsExtractor(Extractor, ABC):
    __DEBIT_PRICE_IND = 1
    __DESCRIPTION_IND = 2
    __TRANSACTION_TYPE_IND = 3
    __TRANSACTION_PRICE_IND = 4
    __COMPANY_IND = 5
    __DATE_IND = 6
    __REFERENCE_IND = None
    __TRANSACTION_DATE_IND = None

    __NUM_OF_COLUMNS = 6

    def __init__(self):
        super().__init__(self.__DATE_IND, self.__COMPANY_IND, self.__DESCRIPTION_IND, self.__TRANSACTION_PRICE_IND,
                         self.__DEBIT_PRICE_IND, self.__REFERENCE_IND,
                         self.__TRANSACTION_DATE_IND, self.__TRANSACTION_TYPE_IND)

    def _update_page_before_extract(self, page: DataFrame) -> None:
        num_of_columns = page.shape[1]
        if num_of_columns < self.__NUM_OF_COLUMNS:
            # The description column is missing
            page.insert(loc=self.__DESCRIPTION_IND - 1, column='description', value=None)

