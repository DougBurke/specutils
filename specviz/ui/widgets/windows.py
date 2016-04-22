from ...third_party.qtpy.QtWidgets import *
from ...third_party.qtpy.QtCore import *
from ...third_party.qtpy.QtGui import *
from ...core.comms import Dispatch, DispatchHandle

from ..qt import icon_resource_rc


class UiMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(UiMainWindow, self).__init__(parent)

        DispatchHandle.setup(self)

        self.resize(1280, 720)
        self.setMinimumSize(QSize(640, 480))
        self.setDockOptions(QMainWindow.AllowTabbedDocks | QMainWindow.AnimatedDocks)
        self.setWindowTitle("SpecViz")

        self.widget_central = QWidget(self)
        self.setCentralWidget(self.widget_central)

        self.layout_vertical = QVBoxLayout(self.widget_central)

        # MDI area setup
        self.mdi_area = QMdiArea(self.widget_central)
        self.mdi_area.setFrameShape(QFrame.StyledPanel)
        self.mdi_area.setFrameShadow(QFrame.Plain)
        self.mdi_area.setLineWidth(2)
        brush = QBrush(QColor(200, 200, 200))
        brush.setStyle(Qt.SolidPattern)
        self.mdi_area.setBackground(brush)

        self.layout_vertical.addWidget(self.mdi_area)

        # Menu bar setup
        self.menu_bar = QMenuBar(self)

        self.menu_file = QMenu(self.menu_bar)
        self.menu_file.setTitle("File")
        self.menu_edit = QMenu(self.menu_bar)
        self.menu_edit.setTitle("Edit")
        self.menu_view = QMenu(self.menu_bar)
        self.menu_edit.setTitle("View")

        self.menu_docks = QMenu(self.menu_bar)

        self.setMenuBar(self.menu_bar)

        # Tool bar setup
        self.tool_bar_main = QToolBar(self)
        self.tool_bar_main.setMovable(False)
        self.tool_bar_main.setFloatable(False)

        self.action_open = QAction(self)
        icon_open= QIcon()
        icon_open.addPixmap(QPixmap(":/img/Open Folder-48.png"))
        self.action_open.setIcon(icon_open)
        self.tool_bar_main.addAction(self.action_open)

        self.addToolBar(Qt.TopToolBarArea, self.tool_bar_main)

        # Status bar setup
        self.status_bar = QStatusBar(self)

        self.setStatusBar(self.status_bar)


class MainWindow(UiMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setup_connections()

    def setup_connections(self):
        self.action_open.triggered.connect(
            lambda: Dispatch.on_file_open.emit())

