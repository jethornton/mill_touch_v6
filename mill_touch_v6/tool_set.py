from functools import partial

def toolSetSetup(parent):
    parent.toolSetKeypad.buttonClicked.connect(partial(toolSetKeypad, parent))
    parent.toolSetBkspBtn.clicked.connect(partial(toolSetBksp, parent))
    parent.toolSetClearBtn.clicked.connect(partial(toolSetClear, parent))

def toolSetKeypad(parent, button):
    char = str(button.text())
    text = parent.toolSetLbl.text() or 'null'
    if text != 'null':
        text += char
    else:
        text = char
    parent.toolSetLbl.setText(text)

def toolSetClear(parent):
    parent.toolSetLbl.setText('')

def toolSetBksp(parent):
    if len(parent.toolSetLbl.text()) > 0:
        text = parent.toolSetLbl.text()[:-1]
        parent.toolSetLbl.setText(text)




