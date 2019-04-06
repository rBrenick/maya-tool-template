__author__ = "Richard Brenick"
__created__ = "2019-01-27"
__modified__ = "2019-04-06"


# Standard
import os

# UI
from . import ui_utils
from ui_utils import QtCore, QtWidgets

# Maya
import pymel.core as pm

# Tool
from . import TOOL_NAME_utils


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
    return TOOL_NAMEWindow()


if __name__ == '__main__':
    main()
