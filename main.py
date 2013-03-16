from galaga_esque import GalagaEsque
from PySide.QtGui import QApplication

import sys

def main(args):
    """ Run the main file """
    app = QApplication(sys.argv)
    galaga = GalagaEsque()
    galaga.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main(sys.argv[1:])