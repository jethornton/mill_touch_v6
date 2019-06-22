from functools import partial

def setupProbe(parent):
    parent.probeKeypad.buttonClicked.connect(partial(handleKeys, parent))
    parent.probeBkspBtn.clicked.connect(partial(backSpace, parent))
    parent.probeClearBtn.clicked.connect(partial(clearLabel, parent))

def handleKeys(parent, button):
    print(parent.probeBtnGrp.checkedButton().property('labelName'))
    entryPoint = parent.probeBtnGrp.checkedButton().property('labelName')
    probeLabel = getattr(parent, entryPoint)
    char = str(button.text())
    text = probeLabel.text() or 'null'
    if text != 'null':
        text += char
    else:
        text = char
    probeLabel.setText(text)


def backSpace(parent):
    entryPoint = parent.probeBtnGrp.checkedButton().property('labelName')
    probeLabel = getattr(parent, entryPoint)
    if len(drillLabel.text()) > 0:
        text = probeLabel.text()[:-1]
        probeLabel.setText(text)

def clearLabel(parent):
    entryPoint = parent.probeBtnGrp.checkedButton().property('labelName')
    probeLabel = getattr(parent, entryPoint)
    probeLabel.setText('')





