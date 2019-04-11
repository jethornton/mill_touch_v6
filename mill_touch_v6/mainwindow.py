from qtpyvcp.widgets.form_widgets.main_window import VCPMainWindow

# Setup logging
from qtpyvcp.utilities import logger
LOG = logger.getLogger('qtpyvcp.' + __name__)

class MyMainWindow(VCPMainWindow):
    """Main window class for the VCP."""
    def __init__(self, *args, **kwargs):
        super(MyMainWindow, self).__init__(*args, **kwargs)

        self.droNavBtnGrp.buttonClicked.connect(self.droChangePage)
        self.mainNavBtnGroup.buttonClicked.connect(self.mainChangePage)
        self.sideBtnGroup.buttonClicked.connect(self.sideChangePage)

    def mainChangePage(self, button):
        self.mainStkWidget.setCurrentIndex(button.property('page'))
        if button.property('buttonName'):
            getattr(self, button.property('buttonName')).setChecked(True)

    def sideChangePage(self, button):
        self.sideStkWiget.setCurrentIndex(button.property('page'))
        if button.property('buttonName'):
            getattr(self, button.property('buttonName')).setChecked(True)


    def droChangePage(self, button):
        self.droStkWidget.setCurrentIndex(button.property('page'))


    def on_exitAppBtn_clicked(self):
        self.app.quit()

