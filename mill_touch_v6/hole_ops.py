from functools import partial

def setupHoleOps(parent):
    parent.holeOpKeypad.buttonClicked.connect(partial(holeOpsKeypad, parent))
    parent.holeOpBkspBtn.clicked.connect(partial(holeOpsBackSpace, parent))
    parent.coordListDownBtn.clicked.connect(partial(coordListDown, parent))
    parent.coordListUpBtn.clicked.connect(partial(coordListUp, parent))
    parent.coordListAppendBtn.clicked.connect(partial(coordListAppend, parent))
    parent.coordListDelLineBtn.clicked.connect(partial(coordListDelLine, parent))
    parent.coordListClearBtn.clicked.connect(partial(coordListClear, parent))



def holeOpsKeypad(parent, button):
    entryPoint = parent.holeOpBtnGrp.checkedButton().property('labelName')
    drillLabel = getattr(parent, entryPoint)
    char = str(button.text())
    text = drillLabel.text() or 'null'
    if text != 'null':
        text += char
    else:
        text = char
    drillLabel.setText(text)


def holeOpsBackSpace(parent):
    entryPoint = parent.holeOpBtnGrp.checkedButton().property('labelName')
    drillLabel = getattr(parent, entryPoint)
    if len(drillLabel.text()) > 0:
        text = drillLabel.text()[:-1]
        drillLabel.setText(text)


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
       if not parent.xCoordRetain.isChecked():
         parent.xCoordLbl.setText('')
    if len(parent.yCoordLbl.text()) > 0:
       coords += 'Y' + parent.yCoordLbl.text() + ' '
       if not parent.yCoordRetain.isChecked():
         parent.yCoordLbl.setText('')
    if len(parent.zCoordLbl.text()) > 0:
       coords += 'Z' + parent.zCoordLbl.text()
       if not parent.zCoordRetain.isChecked():
         parent.zCoordLbl.setText('')
    parent.holeOpCoordList.addItem(coords)

def coordListDelLine(parent):
    parent.holeOpCoordList.takeItem(parent.holeOpCoordList.currentRow())

def coordListClear(parent):
    parent.holeOpCoordList.clear()





