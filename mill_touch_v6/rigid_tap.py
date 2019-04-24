from functools import partial

from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDataWidgetMapper

def rtSetup(parent):
    parent.rtFormFwdBtn.clicked.connect(partial(rtFormFwd, parent))
    parent.rtFormBackBtn.clicked.connect(partial(rtFormBack, parent))
    rtFormInit(parent)

def rtFormInit(parent):
    parent.rtFormMapper = QDataWidgetMapper(parent)
    parent.rtFormModel = QSqlQueryModel(parent)
    parent.rtFormModel.setQuery('SELECT DISTINCT form FROM tap')
    parent.rtFormMapper.setModel(parent.rtFormModel)
    parent.rtFormMapper.addMapping(parent.rtFormLbl, 0, b'text')
    parent.rtFormMapper.toLast()
    parent.rtFormLast = parent.rtFormMapper.currentIndex()
    parent.rtFormMapper.toFirst()
    #threadClassInit(parent)


def rtFormFwd(parent):
    if parent.rtFormMapper.currentIndex() != parent.rtFormLast:
        parent.rtFormMapper.toNext()
    else:
        parent.rtFormMapper.toFirst()
    #threadClassInit(parent)

def rtFormBack(parent):
    if parent.rtFormMapper.currentIndex() != 0:
        parent.rtFormMapper.toPrevious()
    else:
        parent.rtFormMapper.toLast()
    #threadClassInit(parent)






