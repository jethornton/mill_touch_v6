from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

# Setup Button Handler
import mill_touch_v6.nav_handler as navHandler
import mill_touch_v6.mdi_handler as mdiHandler

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        navHandler.setupConnections(self)
        mdiHandler.setupMDI(self)

    def on_exitAppBtn_clicked(self):
        self.app.quit()

