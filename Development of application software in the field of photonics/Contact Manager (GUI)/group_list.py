# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'group_list.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QListWidget,
    QListWidgetItem, QMainWindow, QMenuBar, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Список групп контактов")
        MainWindow.resize(571, 219)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.590909, stop:0 rgba(159, 224, 217, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.hello = QLabel(self.centralwidget)
        self.hello.setObjectName(u"hello")
        self.hello.setEnabled(True)
        self.hello.setMinimumSize(QSize(553, 31))
        self.hello.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.hello.setStyleSheet(u"QLabel {\n"
"    font-family: \"Mustica Pro\";\n"
"    font-size: 20px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")

        self.gridLayout.addWidget(self.hello, 0, 0, 1, 1)

        self.listWidget = QListWidget(self.centralwidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setStyleSheet(u"QListWidget  {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")

        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 571, 22))
        MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(MainWindow)
        # self.statusbar.setObjectName(u"statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Список групп", None))
        self.hello.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0433\u0440\u0443\u043f\u043f", None))
    # retranslateUi

from PySide6.QtWidgets import QMainWindow, QListWidgetItem
from show_group_contacts import ShowGroupContactsWindow  # Окно для показа контактов в группе

class GroupListWindow(QMainWindow):
    def __init__(self, contact_manager, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.manager = contact_manager

        self.load_groups()

        self.ui.listWidget.itemClicked.connect(self.open_group_contacts)  # Обработчик клика

    def load_groups(self):
        """Заполняет список группами из менеджера"""
        self.ui.listWidget.clear()
        if not self.manager.groups:
            self.ui.listWidget.addItem("Групп пока нет.")
            return

        for group, contacts in self.manager.groups.items():
            item = QListWidgetItem(f"{group} ({len(contacts)} контакт(ов))")
            item.setData(32, group)  # Сохраняем имя группы как пользовательские данные
            self.ui.listWidget.addItem(item)

    def open_group_contacts(self, item):
        """Открывает окно с контактами выбранной группы"""
        group_name = item.data(32)  # Получаем имя группы из пользовательских данных
        self.group_contacts_window = ShowGroupContactsWindow(self.manager, group_name, self)
        self.group_contacts_window.show()
