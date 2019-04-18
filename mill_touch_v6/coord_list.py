from functools import partial

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
       parent.xCoordLbl.setText('')
    if len(parent.yCoordLbl.text()) > 0:
       coords += 'Y' + parent.yCoordLbl.text() + ' '
       parent.yCoordLbl.setText('')
    if len(parent.zCoordLbl.text()) > 0:
       coords += 'Z' + parent.zCoordLbl.text()
       parent.zCoordLbl.setText('')
    parent.holeOpCoordList.addItem(coords)




