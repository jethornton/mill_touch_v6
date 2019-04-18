from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

import os
current_path = os.path.dirname(os.path.realpath(__file__)) + '/'

# Setup Button Handler
import mill_touch_v6.nav_handler as navHandler
import mill_touch_v6.mdi_handler as mdiHandler
import mill_touch_v6.g5x_handler as g5xHandler
import mill_touch_v6.g92_handler as g92Handler
import mill_touch_v6.hole_ops as holeOps
import mill_touch_v6.gcode_builder as gcodeBuilder

from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDataWidgetMapper


class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        navHandler.setupNav(self)
        mdiHandler.setupMDI(self)
        g5xHandler.setupG5x(self)
        g92Handler.setupG5x(self)
        holeOps.setupHoleOps(self)
        gcodeBuilder.setupGcodeBuilder(self)

        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(current_path + 'threads0.db')
        if not db.open():
            self.statusbar.showMessage('Database Fucked Up!')


    def on_exitAppBtn_clicked(self):
        self.app.quit()

