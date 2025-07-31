# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_all_contacts.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Полный список контактов")
        MainWindow.resize(571, 169)
        font = QFont()
        font.setFamilies([u"Manrope"])
        font.setPointSize(16)
        MainWindow.setFont(font)
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

        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        font1.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget  {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 571, 22))
        MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(MainWindow) ЗАКОММЕНТИРОВАНО ДЛЯ КРАСОТЫ
        # self.statusbar.setObjectName(u"statusbar") ЗАКОММЕНТИРОВАНО ДЛЯ КРАСОТЫ
        # MainWindow.setStatusBar(self.statusbar) ЗАКОММЕНТИРОВАНО ДЛЯ КРАСОТЫ

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Полный список контактов", None))
        self.hello.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043d\u044b\u0439 \u0441\u043f\u0438\u0441\u043e\u043a \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430", None));
    # retranslateUi

from PySide6.QtWidgets import QMainWindow, QTableWidgetItem

class ShowAllContactsWindow(QMainWindow):
    def __init__(self, contact_manager, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()  # Создаём объект UI
        self.ui.setupUi(self)  # Настраиваем UI
        self.manager = contact_manager  # Получаем экземпляр ContactManager

        self.load_contacts()  # Загружаем контакты в таблицу

    def load_contacts(self):
        """Заполняет таблицу контактами из менеджера"""
        contacts = list(self.manager.contacts.values())
        self.ui.tableWidget.setRowCount(len(contacts))  # Устанавливаем количество строк

        for row, contact in enumerate(contacts):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(contact.name))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(contact.phone_number))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(contact.group or "Без группы"))
