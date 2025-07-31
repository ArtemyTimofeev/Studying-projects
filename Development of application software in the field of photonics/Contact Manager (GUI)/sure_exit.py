# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sure_exit.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(339, 140)
        MainWindow.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.590909, stop:0 rgba(159, 224, 217, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.sure = QLabel(self.centralwidget)
        self.sure.setObjectName(u"sure")
        self.sure.setMinimumSize(QSize(321, 41))
        font = QFont()
        font.setFamilies([u"Mustica Pro"])
        font.setBold(True)
        self.sure.setFont(font)
        self.sure.setStyleSheet(u"QLabel {\n"
"    font-family: \"Mustica Pro\";\n"
"    font-size: 20px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")
        self.sure.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.sure, 0, 0, 1, 2)

        self.yes_Button = QPushButton(self.centralwidget)
        self.yes_Button.setObjectName(u"yes_Button")
        self.yes_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.yes_Button.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular;\n"
"	background: none;\n"
"}\n"
"QPushButton {\n"
"    background-color: #A0A0A0;  /* \u0417\u0435\u043b\u0451\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 10px;        /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #808080;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #404040;  /* \u0415\u0449\u0451 \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430"
                        "\u0442\u0438\u0438 */\n"
"}\n"
"")

        self.gridLayout.addWidget(self.yes_Button, 1, 0, 1, 1)

        self.no_Button = QPushButton(self.centralwidget)
        self.no_Button.setObjectName(u"no_Button")
        self.no_Button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.no_Button.setStyleSheet(u"QPushButton {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular;\n"
"	background: none;\n"
"}\n"
"QPushButton {\n"
"    background-color: #A0A0A0;  /* \u0417\u0435\u043b\u0451\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    color: white;               /* \u0411\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    font-size: 16px;            /* \u0420\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    border-radius: 10px;        /* \u0417\u0430\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 5px 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #808080;  /* \u0422\u0451\u043c\u043d\u043e-\u0441\u0435\u0440\u044b\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #404040;  /* \u0415\u0449\u0451 \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430"
                        "\u0442\u0438\u0438 */\n"
"}\n"
"")

        self.gridLayout.addWidget(self.no_Button, 1, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 339, 22))
        MainWindow.setMenuBar(self.menubar)
        # self.statusbar = QStatusBar(MainWindow) ЗАКОММЕНТИРОВАНО ДЛЯ КРАСОТЫ
        # self.statusbar.setObjectName(u"statusbar") ЗАКОММЕНТИРОВАНО ДЛЯ КРАСОТЫ
        # MainWindow.setStatusBar(self.statusbar) ЗАКОММЕНТИРОВАНО ДЛЯ КРАСОТЫ

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.sure.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b \u0443\u0432\u0435\u0440\u0435\u043d\u044b, \u0447\u0442\u043e \u0445\u043e\u0442\u0438\u0442\u0435 \u0432\u044b\u0439\u0442\u0438?", None))
        self.yes_Button.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430", None))
        self.no_Button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442", None))
    # retranslateUi

from PySide6.QtWidgets import QMainWindow

class SureExitDialog(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()  # Создаём объект UI
        self.ui.setupUi(self)  # Настраиваем UI
        self.setWindowFlags(Qt.FramelessWindowHint)  # Убираем рамку

        # Подключаем кнопки к методам
        self.ui.yes_Button.clicked.connect(self.confirm_exit)
        self.ui.no_Button.clicked.connect(self.close)

        # Центрируем окно относительно родительского окна
        if parent:
            parent_rect = parent.geometry()  # Получаем геометрию родительского окна
            dialog_rect = self.geometry()  # Получаем геометрию диалогового окна
            # Вычисляем координаты для центрирования
            center_x = parent_rect.left() - 280
            center_y = parent_rect.top() - 100
            # Перемещаем диалоговое окно в центр родительского окна
            self.move(center_x, center_y)


    def confirm_exit(self):
        """Закрывает приложение"""
        self.close()  # Закрываем диалог
        self.parent().close()  # Закрываем главное окно
