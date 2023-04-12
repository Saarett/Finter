from abc import ABC

from src.Extractor import Extractor


class LeumiOshExtractor(Extractor, ABC):
    __BALANCE_IND = 1
    __IN_CLEAR_IND = 2
    __IN_DEBT_IND = 3
    __REFERENCE_IND = 4
    __DESCRIPTION_IND = 5
    __VALUE_DATE_IND = 6
    __DATE_IND = 7

    def __init__(self):
        super().__init__(self.__DATE_IND, None, self.__DESCRIPTION_IND, None, None, self.__REFERENCE_IND,
                         self.__VALUE_DATE_IND, None)
