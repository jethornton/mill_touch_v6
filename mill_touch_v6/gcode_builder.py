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
    parent.gcodeDeleteLineBtn.clicked.connect(partial(gcodeDeleteLine, parent))
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
    parent.gCodeList.addItem('; Ream Op')
    if parent.reamToolLbl.text():
        parent.gCodeList.addItem('T{} M6 G43'.format(parent.reamToolLbl.text()))
    if parent.reamRpmLbl.text():
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
    # make sure your using the hole size as the starting point
    parent.gCodeList.addItem('; Single Point Thread Mill Op')
    parent.gCodeList.addItem(';  {}'.format(parent.threadSizeLbl.text()))
    if parent.sptmToolLbl.text():
        parent.gCodeList.addItem('T{} M6 G43'.format(parent.sptmToolLbl.text()))
    if parent.sptmRpmLbl.text():
        parent.gCodeList.addItem('M3 S{}'.format(parent.sptmRpmLbl.text()))
    if parent.sptmCoolantBtn.isChecked():
        parent.gCodeList.addItem('M8')
    parent.gCodeList.addItem('F{}'.format(parent.sptmFeedLbl.text()))
    if parent.gCodeList.count() > 0: # toss out an error if not
        for i in range(parent.holeOpCoordList.count()):
            zClear = parent.sptmZclearLbl.text()
            zStart = parent.sptmZstartLbl.text()
            threadTPI = float(parent.threadTpiLbl.text())
            threadPitch = 1.0 / threadTPI
            threads = float(parent.sptmThreadsLbl.text())
            threadsHeight = (threads + 1) * threadPitch
            numPasses = int(parent.sptmPassesLbl.text())
            majorDia = float(parent.threadMajorDiaLbl.text())
            minorDia = float(parent.sptmHoleDiaLbl.text())
            threadDepth = (majorDia - minorDia)
            sptmCutterDia = float(parent.sptmDiaLbl.text())
            threadCount = int(parent.sptmThreadsLbl.text())
            coordinates = parent.holeOpCoordList.item(i).text()
            parent.gCodeList.addItem('G0 Z{}'.format(zClear))
            parent.gCodeList.addItem('G0 {}'.format(coordinates))
            zEnd = float(zStart) + threadsHeight
            parent.gCodeList.addItem('G1 Z{}'.format(zEnd))
            parent.gCodeList.addItem('G91')
            #parent.gCodeList.addItem('; Thread Passes {}'.format(numPasses))
            for i in range(numPasses):
                parent.gCodeList.addItem('; Thread Pass {}'.format(i))
                passRatios = {1:[1.0], 2:[0.65,1.0], 3:[0.5,0.8,1.0], 4:[0.4,0.67,0.87,1.0]}
                passDiameter = minorDia + (threadDepth * passRatios[numPasses][i])
                parent.gCodeList.addItem('; Pass Diameter {}'.format(passDiameter))
                # go to hole bottom
                parent.gCodeList.addItem('G1 Z-{}'.format(threadsHeight))
                # go to start of lead in arc
                cutterClearance = 0.020
                yStartLeadIn = -((minorDia - (cutterClearance * 2)) - sptmCutterDia) / 2
                parent.gCodeList.addItem('G1 Y{:.4f}'.format(yStartLeadIn))
                # lead in arc
                leadInYEnd = ((passDiameter - sptmCutterDia) / 2) + abs(yStartLeadIn)
                leadInZEnd = threadPitch / 2
                leadInJOffset = leadInYEnd / 2
                parent.gCodeList.addItem('G3 X0.0 Y{:.4f} Z{:.4f} J{:.4f}' \
                    .format(leadInYEnd, leadInZEnd, leadInJOffset))
                # spiral up
                finalZ = threadPitch * threadCount
                jOffset = -(passDiameter - sptmCutterDia) / 2
                parent.gCodeList.addItem('G3 J{} Z{} P{}'. \
                    format(jOffset, finalZ, threadCount))
                # lead out arc
                leadOutYEnd = -((passDiameter - sptmCutterDia) / 2) - abs(yStartLeadIn)
                leadOutZEnd = threadPitch / 2
                leadOutJOffset = -(leadInYEnd / 2)
                parent.gCodeList.addItem('G3 X0.0 Y{:.4f} Z{:.4f} J{:.4f}' \
                    .format(leadOutYEnd, leadOutZEnd, leadOutJOffset))
                # go to center
                yCenter = ((minorDia - (cutterClearance * 2)) - sptmCutterDia) / 2
                parent.gCodeList.addItem('G1 Y{:.4f}'.format(yCenter))
            parent.gCodeList.addItem('G90')

def gcodeExtThreadMill(parent):
    pass

def gcodeMdi(parent):
    parent.gCodeList.addItem(parent.mdiEntry.text())
    parent.mdiEntry.setText('')

def gcodePostAmble(parent):
    pass

def gcodeSave(parent):
    gcode = []
    with open('/home/john/linuxcnc/nc_files/jt-save.ngc','w') as f:
        for i in range(parent.gCodeList.count()):
            gcode.append(parent.gCodeList.item(i).text())
        f.write('\n'.join(gcode))

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

def gcodeDeleteLine(parent):
    parent.gCodeList.takeItem(parent.gCodeList.currentRow())

def gcodeDeleteAll(parent):
    parent.gCodeList.clear()




