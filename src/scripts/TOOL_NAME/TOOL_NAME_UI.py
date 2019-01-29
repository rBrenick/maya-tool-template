__author__ = "Richard Brenick"
__created__ = "2019-01-27"
__modified__ = "2019-01-27"


# Python
import os

# UI
from Qt import QtGui, QtCore, QtWidgets
from . import ui_utils
reload(ui_utils)

# Maya
import pymel.core as pm

# Tool
from . import TOOL_NAME_utils
reload(TOOL_NAME_utils)


# Load UI
UI_FILES_FOLDER = os.path.join(os.path.dirname(__file__), "ui_files")

UI_FILE_MAIN = os.path.join(UI_FILES_FOLDER, "TOOL_NAME_dialog.ui")
UI_FILE_MAIN_FORM, UI_FILE_MAIN_BASE = ui_utils.load_ui_types(UI_FILE_MAIN)


class TOOL_NAMEWindow(UI_FILE_MAIN_FORM, UI_FILE_MAIN_BASE):
    def __init__(self, parent=ui_utils.get_top_window()):
        ui_utils.delete_window(self)
        super(TOOL_NAMEWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.ui_parent = parent
        self.setup_ui()
        self.setup_connections()

        self.show()

    def setup_ui(self):
        pass

    def setup_connections(self):
        self.BTN_example.clicked.connect(self.example_function)

    def example_function(self):
        print("EXAMPLE_BUTTON")


def main():
    return TOOL_NAMEWindow()


if __name__ == '__main__':
    main()
