__author__ = "Richard Brenick"
__created__ = "2019-01-27"
__modified__ = "2019-04-06"


# Standard
import os
import sys

# UI
from TOOL_NAME.ui import ui_utils
from TOOL_NAME.ui.ui_utils import QtCore, QtWidgets

# DCC
# import pymel.core as pm

# Tool
from TOOL_NAME import TOOL_NAME_utils


class TOOL_NAMEWindow(ui_utils.BaseWindow):
    def __init__(self):
        super(TOOL_NAMEWindow, self).__init__(ui_file_name="TOOL_NAME_ui.ui")
        
        self.setup_ui()
        self.setup_connections()

    def setup_ui(self):
        pass

    def setup_connections(self):
        self.ui.example_BTN.clicked.connect(self.example_function)

    def example_function(self):
        print("EXAMPLE_BUTTON")


def main():
    try:
        app = QtWidgets.QApplication(sys.argv)
    except:
        app = None
    
    win = TOOL_NAMEWindow()
    
    if app:
        sys.exit(app.exec_())
    
    return win


if __name__ == '__main__':
    main()
    
    

