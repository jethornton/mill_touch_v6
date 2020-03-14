from functools import partial

def setupBtns(parent):
    parent.plotRollPanBtn.clicked.connect(partial(toggleRollPan, parent))

def toggleRollPan(parent):
  if parent.plotRollPanBtn.isChecked():
    parent.plotRollPanBtn.setText('Pan')
  else:
    parent.plotRollPanBtn.setText('Roll')


