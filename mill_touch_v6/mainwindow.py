from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

# Setup Button Handler
import mill_touch_v6.nav_handler as navHandler
import mill_touch_v6.mdi_handler as mdiHandler
import mill_touch_v6.g5x_handler as g5xHandler
import mill_touch_v6.g92_handler as g92Handler
import mill_touch_v6.hole_ops as holeOps
import mill_touch_v6.gcode_builder as gcodeBuilder

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

    def on_exitAppBtn_clicked(self):
        self.app.quit()

