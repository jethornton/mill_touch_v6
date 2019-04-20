from functools import partial

from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlQuery
from PyQt5.QtWidgets import QDataWidgetMapper

import os
current_path = os.path.dirname(os.path.realpath(__file__)) + '/'

def toolTableSetup(parent):

    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(current_path + 'tools.db')
    if db.open():
        print("Connection success !")
    else:
        print("Connection failed !\n{}".format(db.lastError().text()))

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









