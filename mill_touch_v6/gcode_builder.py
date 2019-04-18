from functools import partial

def setupGcodeBuilder(parent):
    parent.gcodePreambleBtn.clicked.connect(partial(gcodePreamble, parent))
    parent.gcodeSpotBtn.clicked.connect(partial(gcodeSpot, parent))
    parent.gcodeDrillBtn.clicked.connect(partial(gcodeDrill, parent))
    parent.gcodeChamferBtn.clicked.connect(partial(gcodeChamfer, parent))

    parent.gcodeMoveUpBtn.clicked.connect(partial(gcodeMoveUp, parent))
    parent.gcodeMoveDownBtn.clicked.connect(partial(gcodeMoveDown, parent))



    parent.gcodeDeleteAllBtn.clicked.connect(partial(gcodeDeleteAll, parent))


def gcodePreamble(parent):
    parent.gCodeList.addItem("; JT's G code wizard")
    parent.gCodeList.addItem(parent.gcodePreambleLbl.text())

def gcodeSpot(parent):
    parent.gCodeList.addItem('; Spot Op')
    if parent.spotToolLbl.text():
        parent.gCodeList.addItem('T{} M6 G43'.format(parent.spotToolLbl.text()))
    if parent.spotRpmLbl.text():
        parent.gCodeList.addItem('M3 S{}'.format(parent.spotRpmLbl.text()))
    if parent.spotCoolantBtn.isChecked():
        parent.gCodeList.addItem('M8')
    if parent.spotFeedLbl.text():
        parent.gCodeList.addItem('F{}'.format(parent.spotFeedLbl.text()))
    if parent.holeOpCoordList.count() > 0: # toss out an error if not
        for i in range(parent.holeOpCoordList.count()):
            coordinates = parent.holeOpCoordList.item(i).text()
            zEnd = parent.spotZEndLbl.text()
            zRetract = parent.spotZRetractLbl.text()
            if i == 0:
                parent.gCodeList.addItem('G81 {} Z{} R{}'.format(coordinates, zEnd, zRetract))
            else:
                parent.gCodeList.addItem('{}'.format(coordinates))
        parent.gCodeList.addItem('G80 M5 M9')

def gcodeDrill(parent):
    parent.gCodeList.addItem('; Drill Op')
    if parent.drillToolLbl.text():
        parent.gCodeList.addItem('T{} M6 G43'.format(parent.drillToolLbl.text()))
    if parent.drillRpmLbl.text():
        parent.gCodeList.addItem('M3 S{}'.format(parent.drillRpmLbl.text()))
    if parent.drillCoolantBtn.isChecked():
        parent.gCodeList.addItem('M8')
    if parent.drillFeedLbl.text():
        parent.gCodeList.addItem('F{}'.format(parent.drillFeedLbl.text()))
    if parent.gCodeList.count() > 0: # toss out an error if not
        for i in range(parent.holeOpCoordList.count()):
            coordinates = parent.holeOpCoordList.item(i).text()
            zEnd = parent.drillZEndLbl.text()
            zRetract = parent.drillZRetractLbl.text()
            if i == 0:
                parent.gCodeList.addItem('G81 {} Z{} R{}'.format(coordinates, zEnd, zRetract))
            else:
                parent.gCodeList.addItem('{}'.format(coordinates))
        parent.gCodeList.addItem('G80 M5 M9')

def gcodeChamfer(parent):
    parent.gCodeList.addItem('; Chamfer Op')
    if parent.chamferToolLbl.text():
        parent.gCodeList.addItem('T{} M6 G43'.format(parent.chamferToolLbl.text()))
    if parent.chamferRpmLbl.text():
        parent.gCodeList.addItem('M3 S{}'.format(parent.chamferRpmLbl.text()))
    if parent.chamferCoolantBtn.isChecked():
        parent.gCodeList.addItem('M8')
    if parent.chamferFeedLbl.text():
        parent.gCodeList.addItem('F{}'.format(parent.chamferFeedLbl.text()))
    if parent.gCodeList.count() > 0: # toss out an error if not
        for i in range(parent.holeOpCoordList.count()):
            coordinates = parent.holeOpCoordList.item(i).text()
            zEnd = parent.chamferZEndLbl.text()
            zRetract = parent.chamferZRetractLbl.text()
            if i == 0:
                parent.gCodeList.addItem('G81 {} Z{} R{}'.format(coordinates, zEnd, zRetract))
            else:
                parent.gCodeList.addItem('{}'.format(coordinates))
        parent.gCodeList.addItem('G80 M5 M9')


def gcodeMoveDown(parent):
    rows = parent.gCodeList.count()-1
    currentRow = parent.gCodeList.currentRow()
    if currentRow < rows:
        parent.gCodeList.setCurrentRow(currentRow + 1)
    else:
        parent.gCodeList.setCurrentRow(0)

def gcodeMoveUp(parent):
    rows = parent.gCodeList.count()-1
    currentRow = parent.gCodeList.currentRow()
    if currentRow > 0:
        parent.gCodeList.setCurrentRow(currentRow - 1)
    else:
        parent.gCodeList.setCurrentRow(rows)



def gcodeDeleteAll(parent):
    parent.gCodeList.clear()




