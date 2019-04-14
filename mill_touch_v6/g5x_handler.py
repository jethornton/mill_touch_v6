from functools import partial

def setupG5x(parent):
    parent.g5xBtnGrp.buttonClicked.connect(partial(g5xKeypad, parent))
    parent.g5xBkspBtn.clicked.connect(partial(g5xBackSpace, parent))


def g5xKeypad(parent, button):
    char = str(button.text())
    text = parent.g5xOffsetLbl.text() or 'null'
    if text != 'null':
        text += char
    else:
        text = char
    parent.g5xOffsetLbl.setText(text)

def g5xBackSpace(parent):
    if len(parent.g5xOffsetLbl.text()) > 0:
        text = parent.g5xOffsetLbl.text()[:-1]
        parent.g5xOffsetLbl.setText(text)
