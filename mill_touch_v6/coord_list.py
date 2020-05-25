from functools import partial

"""
This is no longer used, code is in hole_ops.py

def setupCoordList(parent):
    parent.coordListDownBtn.clicked.connect(partial(coordListDown, parent))
    parent.coordListUpBtn.clicked.connect(partial(coordListUp, parent))
    parent.coordListAppendBtn.clicked.connect(partial(coordListAppend, parent))


def coordListDown(parent):
    rows = parent.holeOpCoordList.count()-1
    currentRow = parent.holeOpCoordList.currentRow()
    if currentRow < rows:
        parent.holeOpCoordList.setCurrentRow(currentRow + 1)
    else:
        parent.holeOpCoordList.setCurrentRow(0)


def coordListUp(parent):
    rows = parent.holeOpCoordList.count()-1
    currentRow = parent.holeOpCoordList.currentRow()
    if currentRow > 0:
        parent.holeOpCoordList.setCurrentRow(currentRow - 1)
    else:
        parent.holeOpCoordList.setCurrentRow(rows)

def coordListAppend(parent):
    coords = ''
    if len(parent.xCoordLbl.text()) > 0:
       coords = 'X' + parent.xCoordLbl.text() + ' '
       if not self.xCoordRetain.isChecked():
         parent.xCoordLbl.setText('')
    if len(parent.yCoordLbl.text()) > 0:
       coords += 'Y' + parent.yCoordLbl.text() + ' '
       if not self.yCoordRetain.isChecked():
         parent.yCoordLbl.setText('')
    if len(parent.zCoordLbl.text()) > 0:
       coords += 'Z' + parent.zCoordLbl.text()
       if not self.zCoordRetain.isChecked():
         parent.zCoordLbl.setText('')
    parent.holeOpCoordList.addItem(coords)

"""


