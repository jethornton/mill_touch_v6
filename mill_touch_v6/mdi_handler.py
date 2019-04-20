# Setup Help Text
import mill_touch_v6.mdi_text as mdiText

from functools import partial

def setupMDI(parent):
    parent.mdiKeypad.buttonClicked.connect(partial(mdiKeypad, parent))
    parent.mdiNavBtns.buttonClicked.connect(partial(mdiChangePage, parent))
    parent.mdiBackspace.clicked.connect(partial(mdiBackSpace, parent))
    parent.mdiSetLabelsBtn.clicked.connect(partial(mdiSetLabels, parent))
    parent.mdiSendBtn.clicked.connect(partial(mdiClear, parent))
    parent.gcodeListPageUpBtn.clicked.connect(partial(gcodeListPageUp, parent))
    parent.gcodeListPageDownBtn.clicked.connect(partial(gcodeListPageDown, parent))
    titles = mdiText.gcode_titles()
    for key in sorted(titles.iterkeys()):
        parent.gcodeHelpListWidget.addItem(key + ' ' + titles[key])

def mdiChangePage(parent, button):
    parent.mdiStack.setCurrentIndex(button.property('page'))

def mdiKeypad(parent, button):
    char = str(button.text())
    text = parent.mdiEntry.text() or 'null'
    if text != 'null':
        text += char
    else:
        text = char
    parent.mdiEntry.setText(text)

def mdiSetLabels(parent):
    # get smart and figure out what axes are used

    text = parent.mdiEntry.text() or 'null'
    print(text)
    if text != 'null':
        words = mdiText.gcode_words()
        if text in words:
            mdiClear(parent)
            for index, value in enumerate(words[text], start=1):
                print(value)
                getattr(parent, 'gcodeParameter_' + str(index)).setText(value)
        else:
            mdiClear(parent)
        titles = mdiText.gcode_titles()
        if text in titles:
            parent.gcodeDescription.setText(titles[text])
        else:
            mdiClear(parent)
        parent.gcodeHelpLabel.setText(mdiText.gcode_descriptions(text))
    else:
        mdiClear(parent)
        print('No Match')

def mdiClear(parent):
    for index in range(1,8):
        getattr(parent, 'gcodeParameter_' + str(index)).setText('')
    parent.gcodeDescription.setText('')
    parent.gcodeHelpLabel.setText('')

def mdiBackSpace(parent):
    if len(parent.mdiEntry.text()) > 0:
        text = parent.mdiEntry.text()[:-1]
        parent.mdiEntry.setText(text)

def gcodeListPageUp(parent):
    rows = parent.gcodeHelpListWidget.count()-1
    currentRow = parent.gcodeHelpListWidget.currentRow()
    if currentRow > 0:
        if currentRow > 25:
            parent.gcodeHelpListWidget.setCurrentRow(currentRow - 25)
        else:
            parent.gcodeHelpListWidget.setCurrentRow(0)
    else:
        parent.gcodeHelpListWidget.setCurrentRow(rows)

def gcodeListPageDown(parent):
    rows = parent.gcodeHelpListWidget.count()-1
    currentRow = parent.gcodeHelpListWidget.currentRow()
    if currentRow < rows:
        if (currentRow + 25) < rows:
            parent.gcodeHelpListWidget.setCurrentRow(currentRow + 25)
        else:
            parent.gcodeHelpListWidget.setCurrentRow(rows)
    else:
        parent.gcodeHelpListWidget.setCurrentRow(0)




