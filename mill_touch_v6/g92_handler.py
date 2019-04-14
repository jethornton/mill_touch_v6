from functools import partial

def setupG5x(parent):
    parent.g92Btns.buttonClicked.connect(partial(g92Keypad, parent))
    parent.g92BkspBtn.clicked.connect(partial(g92BackSpace, parent))

def g92Keypad(parent, button):
    char = str(button.text())
    text = parent.g92OffsetsLbl.text() or 'null'
    if text != 'null':
        text += char
    else:
        text = char
    parent.g92OffsetsLbl.setText(text)

def g92BackSpace(parent):
    if len(parent.g92OffsetsLbl.text()) > 0:
        text = parent.g92OffsetsLbl.text()[:-1]
        parent.g92OffsetsLbl.setText(text)





