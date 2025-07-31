# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_contact_manager.ui'
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
from PySide6.QtWidgets import (QApplication, QCommandLinkButton, QLabel, QMainWindow,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_ContactManager(object):
    def setupUi(self, ContactManager):
        if not ContactManager.objectName():
            ContactManager.setObjectName(u"ContactManager")
        ContactManager.resize(571, 354)
        ContactManager.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        ContactManager.setAutoFillBackground(False)
        ContactManager.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.590909, stop:0 rgba(159, 224, 217, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.centralwidget = QWidget(ContactManager)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(571, 311))
        self.btnCreateContact = QCommandLinkButton(self.centralwidget)
        self.btnCreateContact.setObjectName(u"btnCreateContact")
        self.btnCreateContact.setEnabled(True)
        self.btnCreateContact.setGeometry(QRect(9, 69, 224, 42))
        font = QFont()
        font.setFamilies([u"Manrope"])
        self.btnCreateContact.setFont(font)
        self.btnCreateContact.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnCreateContact.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular;\n"
"	background: none;\n"
"}\n"
"")
        self.btnShowAllContacts = QCommandLinkButton(self.centralwidget)
        self.btnShowAllContacts.setObjectName(u"btnShowAllContacts")
        self.btnShowAllContacts.setGeometry(QRect(9, 129, 320, 42))
        self.btnShowAllContacts.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnShowAllContacts.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular;\n"
"	background: none;\n"
"}\n"
"")
        self.btnExit = QCommandLinkButton(self.centralwidget)
        self.btnExit.setObjectName(u"btnExit")
        self.btnExit.setGeometry(QRect(9, 248, 172, 42))
        self.btnExit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnExit.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular;\n"
"	background: none;\n"
"}\n"
"")
        self.btnShowGroups = QCommandLinkButton(self.centralwidget)
        self.btnShowGroups.setObjectName(u"btnShowGroups")
        self.btnShowGroups.setGeometry(QRect(9, 188, 223, 42))
        self.btnShowGroups.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnShowGroups.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular;\n"
"	background: none;\n"
"}\n"
"")
        self.hello = QLabel(self.centralwidget)
        self.hello.setObjectName(u"hello")
        self.hello.setEnabled(True)
        self.hello.setGeometry(QRect(9, 20, 553, 31))
        self.hello.setMinimumSize(QSize(553, 31))
        self.hello.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.hello.setStyleSheet(u"QLabel {\n"
"    font-family: \"Mustica Pro\";\n"
"    font-size: 20px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")
        ContactManager.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ContactManager)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 571, 22))
        ContactManager.setMenuBar(self.menubar)
        #self.statusbar = QStatusBar(ContactManager)
        #self.statusbar.setObjectName(u"statusbar")
        #ContactManager.setStatusBar(self.statusbar)

        self.retranslateUi(ContactManager)

        QMetaObject.connectSlotsByName(ContactManager)
    # setupUi

    def retranslateUi(self, ContactManager):
        ContactManager.setWindowTitle(QCoreApplication.translate("ContactManager", u"Менеджер контактов", None))
        self.btnCreateContact.setText(QCoreApplication.translate("ContactManager", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.btnShowAllContacts.setText(QCoreApplication.translate("ContactManager", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043f\u043e\u043b\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432", None))
        self.btnExit.setText(QCoreApplication.translate("ContactManager", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.btnShowGroups.setText(QCoreApplication.translate("ContactManager", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0441\u043f\u0438\u0441\u043e\u043a \u0433\u0440\u0443\u043f\u043f", None))
        self.hello.setText(QCoreApplication.translate("ContactManager", u"\u0414\u043e\u0431\u0440\u043e \u043f\u043e\u0436\u0430\u043b\u043e\u0432\u0430\u0442\u044c \u0432 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440 \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432!", None))
    # retranslateUi

