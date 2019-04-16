from functools import partial

def setupNav(parent):
    parent.mainNavBtns.buttonClicked.connect(partial(mainChangePage, parent))
    parent.sideNavBtns.buttonClicked.connect(partial(sideChangePage, parent))
    parent.droNavBtns.buttonClicked.connect(partial(droChangePage, parent))
    parent.holeNavBtns.buttonClicked.connect(partial(holeOpsChangePage, parent))

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

def holeOpsChangePage(parent, button):
    parent.holeOps1Stk.setCurrentIndex(button.property('page'))
    parent.holeOps2Stk.setCurrentIndex(button.property('page'))
    if button.property('buttonName'):
        getattr(parent, button.property('buttonName')).setChecked(True)








