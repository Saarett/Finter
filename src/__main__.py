"""
Invokes the main runner of finter.
"""
import sys


class Finter:
    @staticmethod
    def run():
        print(f'First Finter run!!')


if __name__ == '__main__':
    finter = Finter()
    sys.exit(finter.run())
