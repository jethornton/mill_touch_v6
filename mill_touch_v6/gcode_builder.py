from functools import partial
import linuxcnc

def setupGcodeBuilder(parent):
    parent.gcodePreambleBtn.clicked.connect(partial(gcodePreamble, parent))
    parent.gcodeSpotBtn.clicked.connect(partial(gcodeSpot, parent))
    parent.gcodeDrillBtn.clicked.connect(partial(gcodeDrill, parent))
    parent.gcodeChamferBtn.clicked.connect(partial(gcodeChamfer, parent))
    parent.gcodeReamBtn.clicked.connect(partial(gcodeReam, parent))
    parent.gcodeRigidTapBtn.clicked.connect(partial(gcodeRigidTap, parent))
    parent.gcodeFloatingTapBtn.clicked.connect(partial(gcodeFloatingTap, parent))
    parent.gcodeSomeThingBtn.clicked.connect(partial(gcodeSomeThing, parent))
    parent.gcodeIntThreadMillBtn.clicked.connect(partial(gcodeIntThreadMill, parent))
    parent.gcodeExtThreadMillBtn.clicked.connect(partial(gcodeExtThreadMill, parent))
    parent.gcodeMdiBtn.clicked.connect(partial(gcodeMdi, parent))
    parent.gcodePostAmbleBtn.clicked.connect(partial(gcodePostAmble, parent))
    parent.gcodeSaveBtn.clicked.connect(partial(gcodeSave, parent))
    parent.gcodeLoadBtn.clicked.connect(partial(gcodeLoad, parent))

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

def gcodeReam(parent):
    parent.gCodeList.addItem('; Chamfer Op')
    if parent.reamToolLbl.text():
        parent.gCodeList.addItem('T{} M6 G43'.format(parent.reamToolLbl.text()))
    if parent.chamferRpmLbl.text():
        parent.gCodeList.addItem('M3 S{}'.format(parent.reamRpmLbl.text()))
    if parent.reamCoolantBtn.isChecked():
        parent.gCodeList.addItem('M8')
    if parent.reamFeedLbl.text():
        parent.gCodeList.addItem('F{}'.format(parent.reamFeedLbl.text()))
    if parent.gCodeList.count() > 0: # toss out an error if not
        for i in range(parent.holeOpCoordList.count()):
            coordinates = parent.holeOpCoordList.item(i).text()
            zEnd = parent.reamZEndLbl.text()
            zRetract = parent.reamZRetractLbl.text()
            if i == 0:
                parent.gCodeList.addItem('G81 {} Z{} R{}'.format(coordinates, zEnd, zRetract))
            else:
                parent.gCodeList.addItem('{}'.format(coordinates))
        parent.gCodeList.addItem('G80 M5 M9')

def gcodeRigidTap(parent):
    pass

def gcodeFloatingTap(parent):
    pass

def gcodeSomeThing(parent):
    pass

def gcodeIntThreadMill(parent):
    pass

def gcodeExtThreadMill(parent):
    pass

def gcodeMdi(parent):
    parent.gCodeList.addItem(parent.mdiEntry.text())
    parent.mdiEntry.setText('')

def gcodePostAmble(parent):
    pass

def gcodeSave(parent):
    pass

def gcodeLoad(parent):
    emcCommand = linuxcnc.command()
    gcode = []
    with open('/tmp/qtpyvcp.ngc','w') as f:
        for i in range(parent.gCodeList.count()):
            gcode.append(parent.gCodeList.item(i).text())
        f.write('\n'.join(gcode))
    emcCommand.reset_interpreter()
    emcCommand.program_open('/tmp/qtpyvcp.ngc')


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




