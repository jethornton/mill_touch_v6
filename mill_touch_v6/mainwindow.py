from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow
from qtpy.QtCore import Slot
from qtpy.QtWidgets import QAbstractButton
from qtpyvcp.plugins import getPlugin
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtSql import QSqlDatabase

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

import os
current_path = os.path.dirname(os.path.realpath(__file__)) + '/'

# Setup Handlers
import mill_touch_v6.plot_handler as plotHandler
import mill_touch_v6.mdi_handler as mdiHandler
import mill_touch_v6.g5x_handler as g5xHandler
import mill_touch_v6.g92_handler as g92Handler
import mill_touch_v6.hole_ops as holeOps
import mill_touch_v6.probe_handler as probeHandler
import mill_touch_v6.gcode_builder as gcodeBuilder
import mill_touch_v6.rigid_tap as rigidTap
import mill_touch_v6.sptm_inside as sptmInside
import mill_touch_v6.tool_table as toolTable
import mill_touch_v6.tool_set as toolSet

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(current_path + 'threads.db')
        if db.open():
            print("Connection success !")
        else:
            print("Connection failed !\n{}".format(db.lastError().text()))

        plotHandler.setupBtns(self)
        mdiHandler.setupMDI(self)
        g5xHandler.setupG5x(self)
        g92Handler.setupG5x(self)
        holeOps.setupHoleOps(self)
        probeHandler.setupProbe(self)
        gcodeBuilder.setupGcodeBuilder(self)
        rigidTap.rtSetup(self)
        sptmInside.sptmInsideSetup(self)
        toolTable.toolTableSetup(self)
        toolSet.toolSetSetup(self)

    def get_signals(self, source):
        cls = source if isinstance(source, type) else type(source)
        signal = type(QtCore.pyqtSignal())
        for name in dir(source):
            if isinstance(getattr(cls, name), signal):
                print(name)

    @Slot(QAbstractButton)
    def on_mainNavBtns_buttonClicked(self, button):
        self.mainStkWidget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_sideNavBtns_buttonClicked(self, button):
        self.sideStkWiget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_droSmallNavBtns_buttonClicked(self, button):
        self.droSmallStkWidget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_droNavBtns_buttonClicked(self, button):
        self.droStkWidget.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_holeNavBtns_buttonClicked(self, button):
        self.holeOps1Stk.setCurrentIndex(button.property('page'))
        self.holeOps2Stk.setCurrentIndex(button.property('page'))

    @Slot(QAbstractButton)
    def on_notifyNavBtns_buttonClicked(self, button):
        self.notifyStkWidget.setCurrentIndex(button.property('page'))


    def on_exitAppBtn_clicked(self):
        self.app.quit()

