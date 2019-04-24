from functools import partial

from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDataWidgetMapper


def sptmInsideSetup(parent):
    threadFormInit(parent)
    threadClassInit(parent)
    sptmSizeInit(parent)

    parent.threadFormFwdBtn.clicked.connect(partial(threadFormFwd, parent))
    parent.threadFormBackBtn.clicked.connect(partial(threadFormBack, parent))
    parent.threadClassFwdBtn.clicked.connect(partial(threadClassFwd, parent))
    parent.threadClassBackBtn.clicked.connect(partial(threadClassBack, parent))
    parent.threadSizeFwdBtn.clicked.connect(partial(threadSizeFwd, parent))
    parent.threadSizeBackBtn.clicked.connect(partial(threadSizeBack, parent))
    parent.sptmSizeFwdBtn.clicked.connect(partial(sptmSizeFwd, parent))
    parent.sptmSizeBackBtn.clicked.connect(partial(sptmSizeBack, parent))


def threadFormInit(parent):
    parent.formMapper = QDataWidgetMapper(parent)
    parent.formModel = QSqlQueryModel(parent)
    parent.formModel.setQuery('SELECT DISTINCT form FROM internal_threads')
    parent.formMapper.setModel(parent.formModel)
    parent.formMapper.addMapping(parent.threadFormLbl, 0, b'text')
    parent.formMapper.toLast()
    parent.formsLast = parent.formMapper.currentIndex()
    parent.formMapper.toFirst()
    threadClassInit(parent)

def threadFormFwd(parent):
    if parent.formMapper.currentIndex() != parent.formsLast:
        parent.formMapper.toNext()
    else:
        parent.formMapper.toFirst()
    threadClassInit(parent)

def threadFormBack(parent):
    if parent.formMapper.currentIndex() != 0:
        parent.formMapper.toPrevious()
    else:
        parent.formMapper.toLast()
    threadClassInit(parent)

def threadClassInit(parent):
    parent.classMapper = QDataWidgetMapper(parent)
    parent.classModel = QSqlQueryModel(parent)
    form = parent.threadFormLbl.text()
    classSelect = "SELECT DISTINCT class FROM internal_threads \
        WHERE form = '{}'".format(form)
    parent.classModel.setQuery(classSelect)
    parent.classMapper.setModel(parent.classModel)
    parent.classMapper.addMapping(parent.threadClassLbl, 0, b'text')
    parent.classMapper.toLast()
    parent.classLast = parent.classMapper.currentIndex()
    parent.classMapper.toFirst()
    threadSizeInit(parent)

def threadClassFwd(parent):
    if parent.classMapper.currentIndex() != parent.classLast:
        parent.classMapper.toNext()
    else:
        parent.classMapper.toFirst()
    threadSizeInit(parent, parent.sizeMapper.currentIndex())

def threadClassBack(parent):
    if parent.classMapper.currentIndex() != 0:
        parent.classMapper.toPrevious()
    else:
        parent.classMapper.toLast()
    threadSizeInit(parent, parent.sizeMapper.currentIndex())



def threadSizeInit(parent, index = 0):
    parent.sizeMapper = QDataWidgetMapper(parent)
    parent.sizeModel = QSqlQueryModel(parent)
    threadForm = parent.threadFormLbl.text()
    threadClass = parent.threadClassLbl.text()
    sizeSelect = "SELECT size, pitch, major_dia, \
        min_major_dia, max_minor_dia, min_minor_dia, \
        max_pitch_dia, min_pitch_dia FROM internal_threads WHERE form \
        = '{}' AND class = '{}'".format(threadForm, threadClass)
    parent.sizeModel.setQuery(sizeSelect)
    parent.sizeMapper.setModel(parent.sizeModel)
    parent.sizeMapper.addMapping(parent.threadSizeLbl, 0, b'text')
    parent.sizeMapper.addMapping(parent.threadTpiLbl, 1, b'text')
    parent.sizeMapper.addMapping(parent.threadMajorDiaLbl, 2, b'text')
    parent.sizeMapper.addMapping(parent.threadMinMajorDiaLbl, 3, b'text')
    parent.sizeMapper.addMapping(parent.threadMaxMinorDiaLbl, 4, b'text')
    parent.sizeMapper.addMapping(parent.threadMinMinorDiaLbl, 5, b'text')
    parent.sizeMapper.addMapping(parent.threadMaxPitchDiaLbl, 6, b'text')
    parent.sizeMapper.addMapping(parent.threadMinPitchDiaLbl, 7, b'text')
    parent.sizeMapper.toLast()
    parent.sizeLast = parent.sizeMapper.currentIndex()
    parent.sizeMapper.setCurrentIndex(index)
    #drillSizeInit()
    #threadSizeCalc()
    #numPassesCalc()
    #threadHeightCalc()

def threadSizeFwd(parent):
    if parent.sizeMapper.currentIndex() != parent.sizeLast:
        parent.sizeMapper.toNext()
    else:
        parent.sizeMapper.toFirst()
    #drillSizeInit()
    #threadSizeCalc()
    #numPassesCalc()
    #threadHeightCalc()

def threadSizeBack(parent):
    if parent.sizeMapper.currentIndex() != 0:
        parent.sizeMapper.toPrevious()
    else:
        parent.sizeMapper.toLast()
    #drillSizeInit()
    #threadSizeCalc()
    #numPassesCalc()
    #threadHeightCalc()

def sptmSizeInit(parent):
    parent.sptmMapper = QDataWidgetMapper(parent)
    parent.sptmModel = QSqlQueryModel(parent)
    parent.sptmModel.setQuery('SELECT * FROM sptm')
    parent.sptmMapper.setModel(parent.sptmModel)
    parent.sptmMapper.addMapping(parent.sptmSizeLbl, 0, b'text')
    parent.sptmMapper.addMapping(parent.sptmDiaLbl, 1, b'text')
    parent.sptmMapper.addMapping(parent.sptmCrestLbl, 2, b'text')
    parent.sptmMapper.addMapping(parent.sptmMaxDepthLbl, 3, b'text')
    parent.sptmMapper.addMapping(parent.sptmFlutesLbl, 4, b'text')
    parent.sptmMapper.addMapping(parent.sptmNeckDiaLbl, 5, b'text')
    parent.sptmMapper.toLast()
    parent.sptmLast = parent.sptmMapper.currentIndex()
    parent.sptmMapper.toFirst()

def sptmSizeFwd(parent):
    if parent.sptmMapper.currentIndex() != parent.sptmLast:
        parent.sptmMapper.toNext()
    else:
        parent.sptmMapper.toFirst()
    #sptmCalc()

def sptmSizeBack(parent):
    if parent.sptmMapper.currentIndex() != 0:
        parent.sptmMapper.toPrevious()
    else:
        parent.sptmMapper.toLast()
    #sptmCalc()


"""

def threadSizeCalc(self):
    # PDO calculations
    threadMajorDia = float(self.threadMajorDiaLbl.text())
    drillDia = float(self.holeDiaSb.value())
    standardPDO = threadMajorDia - drillDia
    self.sptmThreadingPDOLbl.setText('{:.04f}'.format(standardPDO))
    # Actual thread height = 1/2 PDO
    threadHeightStandard = standardPDO / 2
    self.threadHeightStdLbl.setText('{:.04f}'.format(threadHeightStandard))
    threadTrangleHeight = threadHeightStandard / 0.625
    self.threadTriangleHeightLbl.setText('{:.04f}'.format(threadTrangleHeight))
    threadPushOutAdj = threadTrangleHeight * 0.125
    self.threadPushOutAdjLbl.setText('{:.04f}'.format(threadPushOutAdj))
    threadPDOAdjustOut = threadPushOutAdj * 2
    self.threadPDOAdjustOutLbl.setText('{:.04f}'.format(threadPDOAdjustOut))
    # -2*(Crest*(SQRT(3)/2))
    sptmCrest = float(self.sptmCrestLbl.text())
    threadPDOCrestAdj = -2 * (sptmCrest * (sqrt(3)/2))
    self.threadPDOCrestAdjLbl.setText('{:.04f}'.format(threadPDOCrestAdj))
    finalPDO = standardPDO + threadPDOAdjustOut + threadPDOCrestAdj
    self.threadFinalPDOLbl.setText('{:.04f}'.format(finalPDO))
    # if final PDO is greater than tip height check
    if self.sptmTipHeight > finalPDO:
        self.sptmTipOkLbl.setText('OK')
    else:
        self.sptmTipOkLbl.setText('Tip Too Small')
    # set maximum number of threads
    threadTPI = float(self.threadTPILbl.text())
    threadPitch = 1.0 / threadTPI
    maxDepth = float(self.sptmMaxDepthLbl.text())
    maxThreads = int(maxDepth / threadPitch)


def sptmCalc(self):
    drillDiameter = float(self.holeDiaSb.value())
    sptmCutterDia = float(self.sptmDiaLbl.text())
    if sptmCutterDia < drillDiameter:
        self.sptmDiaOkLbl.setText('Ok')
    else:
        self.sptmDiaOkLbl.setText('TOO BIG!')
    sptmNeckDia = float(self.sptmNeckDiaLbl.text())
    self.sptmTipHeight = sptmCutterDia - sptmNeckDia
    self.sptmTipHeightLbl.setText('{:.4f}'.format(self.sptmTipHeight))

def drillSizeInit(self):
    self.drillMapper = QDataWidgetMapper(self)
    self.drillQueryModel = QSqlQueryModel(self)
    minMinorDia = str(self.minMinorDiaLbl.text())
    maxMinorDia = str(self.maxMinorDiaLbl.text())
    drillSelect = "SELECT * FROM drills WHERE dia >= '{}' \
        AND dia <= '{}'".format(minMinorDia, maxMinorDia)
    self.drillQueryModel.setQuery(drillSelect)
    self.drillMapper.setModel(self.drillQueryModel)
    self.drillMapper.addMapping(self.drillTypeLbl, 0, b'text')
    self.drillMapper.addMapping(self.drillSizeLbl, 1, b'text')
    self.drillMapper.addMapping(self.drillDiaLbl, 2, b'text')
    self.drillMapper.toLast()
    self.drillLast = self.drillMapper.currentIndex()
    self.drillMapper.toFirst()
    # setup hole dia spinbox
    self.holeDiaSb.setMinimum(float(self.minMinorDiaLbl.text()))
    self.holeDiaSb.setMaximum(float(self.maxMinorDiaLbl.text()))
    # setup pitch dia spinbox
    self.pitchDiaSb.setMinimum(float(self.minPitchDiaLbl.text()))
    self.pitchDiaSb.setMaximum(float(self.maxPitchDiaLbl.text()))

    self.sptmCalc()
    self.threadPercent()

def drillSizeFwd(self):
    if self.drillMapper.currentIndex() != self.drillLast:
        self.drillMapper.toNext()
    else:
        self.drillMapper.toFirst()
    self.sptmCalc()
    self.threadPercent()
    self.threadSizeCalc()

def drillSizeBack(self):
    if self.drillMapper.currentIndex() != 0:
        self.drillMapper.toPrevious()
    else:
        self.drillMapper.toLast()
    self.sptmCalc()
    self.threadPercent()
    self.threadSizeCalc()

def threadPercent(self):
    majorDia = float(self.threadMajorDiaLbl.text())
    minorDia = float(self.drillDiaLbl.text())
    # note for metric convert to TPI
    threadPitch = float(self.threadTPILbl.text())
    threadEngagement = ((majorDia - minorDia) * threadPitch) / 0.01299
    self.threadPercentLbl.setText('{:.0f}%'.format(threadEngagement))

def threadHeightCalc(self):
    pitch = 1.0 / float(self.threadTPILbl.text())
    height = self.threadCountSb.value() * pitch
    self.threadsHeight.setText('{:.4f}"'.format(height))

def numPassesCalc(self):
    majorDia = float(self.threadMajorDiaLbl.text())
    minorDia = float(self.holeDiaSb.value())
    threadDepth = (majorDia - minorDia)
    if self.numPassesSP.value() == 1:
        self.passDiaLbl_0.setText('{:.4f}'.format(majorDia))
        self.passDiaLbl_1.setText('')
        self.passDiaLbl_2.setText('')
        self.passDiaLbl_3.setText('')

        self.passPercentLbl_1.setText('100%')
        self.passPercentLbl_2.setText('')
        self.passPercentLbl_3.setText('')
        self.passPercentLbl_4.setText('')

    if self.numPassesSP.value() == 2:

        self.passDiaLbl_0.setText('{:.4f}'.format(minorDia \
            + (threadDepth * 0.65)))
        self.passDiaLbl_1.setText('{:.4f}'.format(majorDia))
        self.passDiaLbl_2.setText('')
        self.passDiaLbl_3.setText('')

        self.passPercentLbl_1.setText('65%')
        self.passPercentLbl_2.setText('35%')
        self.passPercentLbl_3.setText('')
        self.passPercentLbl_4.setText('')

    if self.numPassesSP.value() == 3:
        self.passDiaLbl_0.setText('{:.4f}'.format(minorDia \
            + (threadDepth * 0.50)))
        self.passDiaLbl_1.setText('{:.4f}'.format(minorDia \
            + (threadDepth * 0.80)))
        self.passDiaLbl_2.setText('{:.4f}'.format(majorDia))
        self.passDiaLbl_3.setText('')

        self.passPercentLbl_1.setText('50%')
        self.passPercentLbl_2.setText('30%')
        self.passPercentLbl_3.setText('20%')
        self.passPercentLbl_4.setText('')

    if self.numPassesSP.value() == 4:
        self.passDiaLbl_0.setText('{:.4f}'.format(minorDia \
            + (threadDepth * 0.40)))
        self.passDiaLbl_1.setText('{:.4f}'.format(minorDia \
            + (threadDepth * 0.67)))
        self.passDiaLbl_2.setText('{:.4f}'.format(minorDia \
            + (threadDepth * 0.87)))
        self.passDiaLbl_3.setText('{:.4f}'.format(majorDia))

        self.passPercentLbl_1.setText('40%')
        self.passPercentLbl_2.setText('27%')
        self.passPercentLbl_3.setText('20%')
        self.passPercentLbl_4.setText('13%')

def holeDiaCalc(self):
    majorDia = float(self.threadMajorDiaLbl.text())
    minorDia = self.holeDiaSb.value()
    # note for metric convert to TPI
    threadPitch = float(self.threadTPILbl.text())
    threadEngagement = ((majorDia - minorDia) * threadPitch) / 0.01299
    self.threadPerLbl.setText('{:.1f}%'.format(threadEngagement))


def genGcode(self):
    # make sure your using the hole size as the starting point
    self.gcodeText.setPlainText("; JT's Thread Mill Wizard")
    self.gcodeText.append('; Thread {}'.format(self.threadSizeLbl.text()))
    self.gcodeText.append('F25')
    xCoord = self.xCoord.text()
    yCoord = self.yCoord.text()
    self.gcodeText.append('G0 X{} Y{} Z0.125'.format(xCoord, yCoord))
    zStart = self.zStart.text()
    pitch = 1.0 / float(self.threadTPILbl.text())
    threadsHeight = (self.threadCountSb.value() + 1) * pitch
    zEnd = float(zStart) + threadsHeight
    self.gcodeText.append('G1 Z{}'.format(zEnd))
    self.gcodeText.append('G91')
    self.gcodeText.append('; Number of thread passes {}' \
        .format(self.numPassesSP.value()))
    for i in range(self.numPassesSP.value()):
        passDiameter = float(getattr(self, 'passDiaLbl_' + str(i)).text())
        # go to hole bottom
        threadTPI = float(self.threadTPILbl.text())
        threadPitch = 1.0 / threadTPI
        self.gcodeText.append('G0 Z-{}'.format(threadsHeight))
        # go to start of lead in arc
        cutterClearance = 0.020
        minorDia = float(self.holeDiaSb.value())
        toolDia = float(self.sptmDiaLbl.text())
        yStartLeadIn = -((minorDia - (cutterClearance * 2)) - toolDia) / 2
        self.gcodeText.append('G1 Y{:.4f}'.format(yStartLeadIn))
        # lead in arc
        sptmCutterDia = float(self.sptmDiaLbl.text())
        leadInYEnd = ((passDiameter - sptmCutterDia) / 2) + abs(yStartLeadIn)
        leadInZEnd = threadPitch / 2
        leadInJOffset = leadInYEnd / 2
        self.gcodeText.append('G3 X0.0 Y{:.4f} Z{:.4f} J{:.4f}' \
            .format(leadInYEnd, leadInZEnd, leadInJOffset))
        # spiral up
        threadCount = int(self.threadCountSb.text())
        finalZ = threadPitch * threadCount
        jOffset = -(passDiameter - sptmCutterDia) / 2
        self.gcodeText.append('G3 J{} Z{} P{}'. \
            format(jOffset, finalZ, threadCount))
        # lead out arc
        leadOutYEnd = -((passDiameter - sptmCutterDia) / 2) - abs(yStartLeadIn)
        leadOutZEnd = threadPitch / 2
        leadOutJOffset = -(leadInYEnd / 2)
        self.gcodeText.append('G3 X0.0 Y{:.4f} Z{:.4f} J{:.4f}' \
            .format(leadOutYEnd, leadOutZEnd, leadOutJOffset))
        # go to center
        yCenter = ((minorDia - (cutterClearance * 2)) - toolDia) / 2
        self.gcodeText.append('G1 Y{:.4f}'.format(yCenter))

    self.gcodeText.append('G90')
    #self.gcodeText.append('G0 X2 Y2')
    self.gcodeText.append('M2')

def linearFeedCalc(self):
    # Internal Threads
    # Linear feed * ((Major thread dia - Tool dia) / Major thread dia)
    minorDia = float(self.holeDiaSb.value())
    majorDia = float(self.threadMajorDiaLbl.text())
    cutterDia = float(self.sptmDiaLbl.text())
    linearFeed = self.linearFeedSb.value()
    circularFeed = ((majorDia - cutterDia) / majorDia) * linearFeed
    self.circularFeedLbl.setText('{:.1f}'.format(circularFeed))

def testFwd(self):
    self.gcodeText.append('line du')

def testBack(self):
    pass

def saveFile(self):
    ngcFile = os.path.join(os.getenv("HOME"), 'linuxcnc/nc_files', 'jt.ngc')
    with open(ngcFile, 'w') as f:
       f.write(str(self.gcodeText.toPlainText()))
"""
