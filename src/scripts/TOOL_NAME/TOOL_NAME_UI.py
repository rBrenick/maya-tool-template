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
from . import tool_utils
reload(tool_utils)


# Load UI
ui_file_main = os.path.join(os.path.dirname(__file__), "ui_files", "dialog.ui")
pform_main, pbase_main = ui_utils.load_ui_types(ui_file_main)


class TOOL_NAMEWindow(pform_main, pbase_main):
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
        pass


def main():
    return TOOL_NAMEWindow()


if __name__ == '__main__':
    main()
