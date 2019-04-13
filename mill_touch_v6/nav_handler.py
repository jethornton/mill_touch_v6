from functools import partial

def setupConnections(parent):
    parent.mainNavBtnGroup.buttonClicked.connect(partial(mainChangePage, parent))
    parent.sideNavBtnGroup.buttonClicked.connect(partial(sideChangePage, parent))
    parent.droNavBtnGrp.buttonClicked.connect(partial(droChangePage, parent))

def mainChangePage(parent, button):
    parent.mainStkWidget.setCurrentIndex(button.property('page'))
    if button.property('buttonName'):
        getattr(parent, button.property('buttonName')).setChecked(True)

def sideChangePage(parent, button):
    parent.sideStkWiget.setCurrentIndex(button.property('page'))
    if button.property('buttonName'):
        getattr(parent, button.property('buttonName')).setChecked(True)

def droChangePage(parent, button):
    parent.droStkWidget.setCurrentIndex(button.property('page'))









