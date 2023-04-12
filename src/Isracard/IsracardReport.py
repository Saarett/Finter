from typing import Union, List, Dict, Any

import tabula
import pandas

from pandas import DataFrame

from src.Isracard.IsracardIsraelExtractor import IsracardIsraelExtractor
from src.Isracard.IsracardAbrodExtractor import IsracardAbroadExtractor


class IsracardReport:
    __isracard_israel_extractor = IsracardIsraelExtractor()
    __isracard_abroad_extractor = IsracardAbroadExtractor()

    def __extract_israel_osh(self, df: Union[List[DataFrame], Dict[str, Any]]) -> DataFrame:
        israel_page = df[0]
        return self.__isracard_israel_extractor.extract_report(israel_page)

    def __extract_abroad_osh(self, df: Union[List[DataFrame], Dict[str, Any]]) -> DataFrame:
        abroad_page = df[1]
        return self.__isracard_abroad_extractor.extract_report(abroad_page)

    def extract_osh(self, path: str) -> DataFrame:
        # reads table from pdf file
        df: Union[List[DataFrame], Dict[str, Any]] = tabula.read_pdf(path, pages="all")

        israel_osh = self.__extract_israel_osh(df)
        abroad_osh = self.__extract_abroad_osh(df)
        all_osh = pandas.concat([israel_osh, abroad_osh])
        return all_osh
