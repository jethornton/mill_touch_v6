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

        self.mainNavBtnGroup.buttonClicked.connect(self.mainChangePage)
        self.sideNavBtnGroup.buttonClicked.connect(self.sideChangePage)
        self.droNavBtnGrp.buttonClicked.connect(self.droChangePage)

        # MDI
        self.mdiBtnGrp.buttonClicked.connect(self.mdiHandleKeys)
        self.mdiNavGroup.buttonClicked.connect(self.mdiChangePage)
        self.mdiBackspace.clicked.connect(self.mdiHandleBackSpace)
        self.mdiSetLabelsBtn.clicked.connect(self.mdiSetLabels)

    def mainChangePage(self, button):
        self.mainStkWidget.setCurrentIndex(button.property('page'))
        if button.property('buttonName'):
            getattr(self, button.property('buttonName')).setChecked(True)

    def sideChangePage(self, button):
        self.sideStkWiget.setCurrentIndex(button.property('page'))
        if button.property('buttonName'):
            getattr(self, button.property('buttonName')).setChecked(True)

    def droChangePage(self, button):
        navHandler.droChangePage(self, button)

    def mdiHandleKeys(self, button):
        mdiHandler.mdiHandleKeys(self, button)

    def mdiChangePage(self, button):
        self.mdiStack.setCurrentIndex(button.property('page'))

    def mdiHandleBackSpace(self):
        mdiHandler.mdiHandleBackSpace(self)

    def mdiSetLabels(self):
        mdiHandler.mdiSetLabels(self)


    def on_exitAppBtn_clicked(self):
        self.app.quit()

