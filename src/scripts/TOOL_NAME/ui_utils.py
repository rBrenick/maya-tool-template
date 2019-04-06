
# Standard
import os

# Not even going to pretend to have Maya 2016 support
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from shiboken2 import wrapInstance
from PySide2 import QtUiTools


UI_FILES_FOLDER = os.path.join(os.path.dirname(__file__), "ui_files")
ICON_FOLDER = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "icons") # boy that's a lot of dirname
"""
QT UTILS BEGIN
"""

def get_app_window():
    top_window = None
    try:
        from maya import OpenMayaUI as omui
        maya_main_window_ptr = omui.MQtUtil().mainWindow()
        top_window = wrapInstance(long(maya_main_window_ptr), QtWidgets.QMainWindow)
    except ImportError, e:
        pass
    return top_window


def delete_window(object_to_delete):
    for widget in QtWidgets.QApplication.instance().topLevelWidgets():
        if "__class__" in dir(widget):
            if str(widget.__class__) == str(object_to_delete.__class__):
                widget.deleteLater()
                widget.close()


def load_ui_file(ui_file_name, widget):
    ui_file_path = os.path.join(UI_FILES_FOLDER, ui_file_name) # get full path
    loader = QtUiTools.QUiLoader()
    uifile = QtCore.QFile(ui_file_path)
    uifile.open(QtCore.QFile.ReadOnly)
    ui = loader.load(uifile)
    uifile.close()
    return ui


def create_qicon(icon_path):
    icon_path = icon_path.replace("\\", "/")
    if "/" not in icon_path:
        icon_path = os.path.join(ICON_FOLDER, icon_path+".png") # find in icons folder if not full path
        if not os.path.exists(icon_path):
            return 
    
    return QtGui.QIcon(icon_path)

    
class BaseWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=get_app_window(), ui_file_name=None):
        delete_window(self)
        super(BaseWindow, self).__init__(parent)
        
        self.ui_parent = parent
        self.ui = None
        if ui_file_name:
            self.load_ui(ui_file_name)
        
        self.set_tool_icon("TOOL_NAME_icon")
        
        self.show()
    
    def set_tool_icon(self, icon_name):
        icon = create_qicon(icon_name)
        if icon:
            self.setWindowIcon(icon)
    
    def load_ui(self, ui_file_name):
        self.ui = load_ui_file(ui_file_name, self)
        self.setGeometry(self.ui.rect())
        self.setWindowTitle(self.ui.property("windowTitle"))
        self.setCentralWidget(self.ui)
        
        maya_window_center = self.ui_parent.mapToGlobal(self.ui_parent.rect().center())
        window_offset_x = maya_window_center.x() - self.geometry().width()/2
        window_offset_y = maya_window_center.y() - self.geometry().height()/2
        self.move(window_offset_x, window_offset_y) # move to maya screen center


"""
QT UTILS END
"""
