from functools import partial

from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDataWidgetMapper

def rtSetup(parent):
    parent.rtFormFwdBtn.clicked.connect(partial(rtFormFwd, parent))
    parent.rtFormBackBtn.clicked.connect(partial(rtFormBack, parent))
    parent.rtSizeFwdBtn.clicked.connect(partial(rtSizeFwd, parent))
    parent.rtSizeBackBtn.clicked.connect(partial(rtSizeBack, parent))


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
    rtSizeInit(parent)


def rtFormFwd(parent):
    if parent.rtFormMapper.currentIndex() != parent.rtFormLast:
        parent.rtFormMapper.toNext()
    else:
        parent.rtFormMapper.toFirst()
    rtSizeInit(parent)

def rtFormBack(parent):
    if parent.rtFormMapper.currentIndex() != 0:
        parent.rtFormMapper.toPrevious()
    else:
        parent.rtFormMapper.toLast()
    rtSizeInit(parent)

def rtSizeInit(parent):
    parent.rtSizeMapper = QDataWidgetMapper(parent)
    parent.rtSizeModel = QSqlQueryModel(parent)
    form = parent.rtFormLbl.text()
    classSelect = "SELECT DISTINCT size FROM tap \
        WHERE form = '{}'".format(form)
    parent.rtSizeModel.setQuery(classSelect)
    parent.rtSizeMapper.setModel(parent.rtSizeModel)
    parent.rtSizeMapper.addMapping(parent.rtSizeLbl, 0, b'text')
    parent.rtSizeMapper.toLast()
    parent.rtSizeLast = parent.rtSizeMapper.currentIndex()
    parent.rtSizeMapper.toFirst()

def rtSizeFwd(parent):
    if parent.rtSizeMapper.currentIndex() != parent.rtSizeLast:
        parent.rtSizeMapper.toNext()
    else:
        parent.rtSizeMapper.toFirst()

def rtSizeBack(parent):
    if parent.rtSizeMapper.currentIndex() != 0:
        parent.rtSizeMapper.toPrevious()
    else:
        parent.rtSizeMapper.toLast()






