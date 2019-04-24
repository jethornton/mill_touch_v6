from functools import partial

from PyQt5.QtSql import QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDataWidgetMapper

def toolTableSetup(parent):
    toolTypeInit(parent)

def toolTypeInit(parent):
    parent.toolTypeMapper = QDataWidgetMapper(parent)
    parent.toolTypeModel = QSqlQueryModel(parent)
    parent.toolTypeModel.setQuery('SELECT DISTINCT material FROM end_mills')
    parent.toolTypeMapper.setModel(parent.toolTypeModel)
    parent.toolTypeMapper.addMapping(parent.endMillMaterialLbl, 0, b'text')
    parent.toolTypeMapper.toLast()
    parent.toolTypeLast = parent.toolTypeMapper.currentIndex()
    print('current index {}'.format(parent.toolTypeMapper.currentIndex()))
    parent.toolTypeMapper.toFirst()









