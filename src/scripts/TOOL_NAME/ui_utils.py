# content

from Qt import QtGui, QtCore, QtWidgets, QtCompat

"""
QT UTILS BEGIN
"""


def get_top_window():
    top_window = None
    try:
        from maya import OpenMayaUI as omui
        maya_main_window_ptr = omui.MQtUtil().mainWindow()
        top_window = QtCompat.wrapInstance(long(maya_main_window_ptr), QtWidgets.QWidget)
    except ImportError, e:
        pass
    return top_window


def delete_window(object_to_delete):
    for widget in QtWidgets.QApplication.instance().topLevelWidgets():
        if "__class__" in dir(widget):
            if str(widget.__class__) == str(object_to_delete.__class__):
                widget.deleteLater()
                widget.close()


def load_ui_types(uifile):
    """
    Ripped from
    https://github.com/mottosso/Qt.py/blob/master/examples/loadUi/baseinstance2.py

    :param uifile:
    :return:
    """
    import xml.etree.ElementTree as ElementTree
    from cStringIO import StringIO

    parsed = ElementTree.parse(uifile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text

    with open(uifile, 'r') as f:
        o = StringIO()
        frame = {}

        try:
            import pyside2uic as pysideuic
        except ImportError:
            import pysideuic as pysideuic

        pysideuic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec(pyc) in frame

        # Fetch the base_class and form class based on their type in
        # the xml from designer
        form_class = frame['Ui_%s' % form_class]
        base_class = eval('QtWidgets.%s' % widget_class)
    return form_class, base_class


"""
QT UTILS END
"""
