from typing import Union, List, Dict, Any

import tabula
import pandas

from pandas import DataFrame

from src.Leumi.LeumiCardsExtractor import LeumiCardsExtractor
from src.Leumi.LeumiOshExtractor import LeumiOshExtractor


class LeumiReport:
    __leumi_osh_extractor = LeumiOshExtractor()
    __leumi_cards_extractor = LeumiCardsExtractor()


    def __extract_osh(self, df: Union[List[DataFrame], Dict[str, Any]]) -> DataFrame:
        osh_pages = df
        osh_pages_reports = []
        for page in osh_pages:
            osh_pages_reports.append(self.__leumi_osh_extractor.extract_report(page))
        return pandas.concat(osh_pages_reports)

    def __extract_cards(self, df: Union[List[DataFrame], Dict[str, Any]]) -> DataFrame:
        osh_pages = df
        osh_pages_reports = []
        for page in osh_pages:
            osh_pages_reports.append(self.__leumi_cards_extractor.extract_report(page))
        return pandas.concat(osh_pages_reports)

    def extract_osh(self, path: str) -> DataFrame:
        # reads table from pdf file
        df: Union[List[DataFrame], Dict[str, Any]] = tabula.read_pdf(path, pages="all")

        # osh = self.__extract_osh(df)
        cards = self.__extract_cards(df)
        all_osh = pandas.concat([cards])
        return all_osh
