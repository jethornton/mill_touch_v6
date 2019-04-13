# Setup Help Text
import mill_touch_v6.mdi_text as mdiText

from functools import partial

def setupConnections(parent):
    parent.mdiBtnGrp.buttonClicked.connect(partial(mdiHandleKeys, parent))
    parent.mdiNavGroup.buttonClicked.connect(partial(mdiChangePage, parent))
    parent.mdiBackspace.clicked.connect(partial(mdiHandleBackSpace, parent))
    parent.mdiSetLabelsBtn.clicked.connect(partial(mdiSetLabels, parent))

def mdiChangePage(parent, button):
    parent.mdiStack.setCurrentIndex(button.property('page'))

def mdiHandleKeys(parent, button):
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

def mdiHandleBackSpace(parent):
    if len(parent.mdiEntry.text()) > 0:
        text = parent.mdiEntry.text()[:-1]
        parent.mdiEntry.setText(text)

