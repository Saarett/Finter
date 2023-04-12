"""
Invokes the main runner of finter.
"""
import sys

from src.Isracard.IsracardReport import IsracardReport
from src.Leumi.LeumiReport import LeumiReport


class Finter:
    def __init__(self):
        self.__leumi_report = LeumiReport()
        self.__isracard_report = IsracardReport()

    def run(self):
        leumi_osh = self.__leumi_report.extract_osh("*")
        print(f'DATE VALUE_DATE DESCRIPTION REFERENCE IN_DEBT IN_CLEAR BALANCE')
        print(leumi_osh)
        # isracard = self.__isracard_report.extract_osh("*")
        # print('DATE VALUE_DATE DESCRIPTION REFERENCE IN_DEBT IN_CLEAR BALANCE')
        # print(isracard)


if __name__ == '__main__':
    finter = Finter()
    finter.run()
    sys.exit()
