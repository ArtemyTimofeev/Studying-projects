# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show_group_contacts.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton, QInputDialog, QMessageBox
from PySide6.QtCore import Qt
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"Список групп контактов")
        MainWindow.resize(571, 304)
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
        self.hello = QLabel(self.centralwidget)
        self.hello.setObjectName(u"hello")
        self.hello.setEnabled(True)
        self.hello.setGeometry(QRect(9, 9, 553, 31))
        self.hello.setMinimumSize(QSize(553, 31))
        self.hello.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.hello.setStyleSheet(u"QLabel {\n"
"    font-family: \"Mustica Pro\";\n"
"    font-size: 20px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(49, 46, 501, 211))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        font1 = QFont()
        font1.setFamilies([u"Manrope"])
        font1.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"QTableWidget  {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout.addWidget(self.tableWidget)


        self.verticalLayout.addLayout(self.horizontalLayout)

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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Список групп", None))
        self.hello.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u043e\u043d\u0442\u0430\u043a\u0442\u043e\u0432 \u0432 \u0433\u0440\u0443\u043f\u043f\u0435 <GROUPNAME>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430", None));
        # retranslateUi



class ShowGroupContactsWindow(QMainWindow):
    def __init__(self, contact_manager, group_name, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.manager = contact_manager
        self.group_name = group_name

        self.setWindowTitle(f"Контакты в группе: {self.group_name}")
        self.ui.hello.setText(f"Список контактов в группе {self.group_name}")

        self.load_contacts()

    def load_contacts(self): # заполнение таблицы контактами
        contacts = self.manager.groups.get(self.group_name, [])
        self.ui.tableWidget.setRowCount(len(contacts))
        self.ui.tableWidget.setColumnCount(3)  # Имя, номер, кнопка "Редактировать"
        self.ui.tableWidget.setHorizontalHeaderLabels(["Имя", "Номер", " "])

        for row, contact in enumerate(contacts):
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(contact.name))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(contact.phone_number))

            edit_button = QPushButton("Редактировать")
            edit_button.clicked.connect(lambda _, r=row: self.edit_contact(r))
            self.ui.tableWidget.setCellWidget(row, 2, edit_button)

    def edit_contact(self, row): # функция редактирования
        name = self.ui.tableWidget.item(row, 0).text()
        phone_number = self.ui.tableWidget.item(row, 1).text()

        # проверка на наличие контакта
        contact = self.manager.contacts.get((phone_number, name))
        if not contact:
            QMessageBox.warning(self, "Ошибка", "Контакт не найден!")
            return

        msg = QMessageBox(self)
        msg.setWindowTitle("Выбор редактирования")
        msg.setText("Что вы хотите изменить?")
        msg.setIcon(QMessageBox.Question)

        # Создаём кнопки "Имя" и "Номер"
        btn_name = msg.addButton("Имя", QMessageBox.AcceptRole)
        btn_number = msg.addButton("Номер", QMessageBox.AcceptRole)
        msg.addButton("Отмена", QMessageBox.RejectRole)

        # Настраиваем стиль
        style = """
            QMessageBox, QInputDialog {
                font-family: 'Manrope';
                font-size: 14px;
            }
            QLabel {
                background: none;
            }
            QLineEdit {
                font-family: 'Mustica Pro';
                font-size: 12px;
                background-color: white;
                border: 1px solid #ced4da;
                padding: 5px;
            }
            QPushButton {
                font-family: 'Mustica Pro';
                font-size: 12px;
                background-color: #007bff;
                color: white;
                border-radius: 5px;
                padding: 6px 12px;
            }
            QPushButton:hover {
                background-color: #0056b3;
            }
        """

        msg.setStyleSheet(style)
        msg.exec()

        # Определяем, какая кнопка была нажата
        if msg.clickedButton() == btn_name:
            choice = "Имя"
        elif msg.clickedButton() == btn_number:
            choice = "Номер"
        else:
            return  # Если нажали "Отмена", выходим

        # Запрос нового имени
        if choice == "Имя":
            dialog = QInputDialog(self)
            dialog.setWindowTitle("Редактирование имени")
            dialog.setLabelText("Введите новое имя:")
            dialog.setTextValue(name)
            dialog.setStyleSheet(style)

            if dialog.exec():
                new_name = dialog.textValue().strip()
                if new_name:
                    if self.manager.change_contact_name(phone_number, new_name):
                        success_msg = QMessageBox()
                        success_msg.setWindowTitle("Успех")
                        success_msg.setText("Имя контакта обновлено!")
                        success_msg.setIcon(QMessageBox.Information)
                        success_msg.setStyleSheet(style)
                        success_msg.exec()

                        self.load_contacts()
                    else:
                        error_msg = QMessageBox()
                        error_msg.setWindowTitle("Ошибка")
                        error_msg.setText("Контакт с таким именем уже существует!")
                        error_msg.setIcon(QMessageBox.Warning)
                        error_msg.setStyleSheet(style)
                        error_msg.exec()

        # Запрос нового номера
        elif choice == "Номер":
            dialog = QInputDialog(self)
            dialog.setWindowTitle("Редактирование номера")
            dialog.setLabelText("Введите новый номер:")
            dialog.setTextValue(phone_number)
            dialog.setStyleSheet(style)

            if dialog.exec():
                new_number = dialog.textValue().strip()
                if new_number:
                    formatted_number = self.manager.format_phone_number(new_number)

                    # Удаляем старый контакт и создаем новый
                    self.manager.delete_contact(phone_number)
                    contact.phone_number = formatted_number  # Обновляем номер
                    self.manager.add_contact(contact)

                    success_msg = QMessageBox()
                    success_msg.setWindowTitle("Успех")
                    success_msg.setText("Номер контакта обновлен!")
                    success_msg.setIcon(QMessageBox.Information)
                    success_msg.setStyleSheet(style)
                    success_msg.exec()

                    self.load_contacts()
