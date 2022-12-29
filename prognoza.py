# imports
from PyQt5 import uic, QtWidgets
import sys

# load ui file
baseUIClass, baseUIWidget = uic.loadUiType("prognoza-ui.ui")

# use loaded ui file in the logic class
class Logic(baseUIWidget, baseUIClass):
    def __init__(self, parent=None):
        super(Logic, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    ui = Logic(None)
    ui.showMaximized()
    sys.exit(app.exec_())