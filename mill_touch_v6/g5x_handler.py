


def g5xHandleKeys(parent, button):
    char = str(button.text())
    text = parent.g5xOffsetLbl.text() or 'null'
    if text != 'null':
        text += char
    else:
        text = char
    parent.g5xOffsetLbl.setText(text)

def g5xHandleBackSpace(parent):
    if len(parent.g5xOffsetLbl.text()) > 0:
        text = parent.g5xOffsetLbl.text()[:-1]
        parent.g5xOffsetLbl.setText(text)
