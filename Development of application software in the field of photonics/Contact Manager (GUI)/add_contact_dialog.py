# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_contact_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from contact_manager import Contact
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, QRegularExpression)
from PySide6.QtGui import (QRegularExpressionValidator, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QMessageBox, QDialog, QGridLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 233)
        Dialog.setStyleSheet(u"QWidget {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.590909, stop:0 rgba(159, 224, 217, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nameInput = QLineEdit(Dialog)
        self.nameInput.setObjectName(u"nameInput")
        self.nameInput.setStyleSheet(u"QLineEdit {background: none;}")

        self.gridLayout.addWidget(self.nameInput, 1, 2, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    font-family: \"Mustica Pro\";\n"
"    font-size: 20px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.phoneInput = QLineEdit(Dialog)
        self.phoneInput.setObjectName(u"phoneInput")
        self.phoneInput.setStyleSheet(u"QLineEdit {background: none;}")

        self.gridLayout.addWidget(self.phoneInput, 2, 2, 1, 1)

        self.groupInput = QLineEdit(Dialog)
        self.groupInput.setObjectName(u"groupInput")
        self.groupInput.setStyleSheet(u"QLineEdit {background: none;}")

        self.gridLayout.addWidget(self.groupInput, 3, 2, 1, 1)

        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.cancelButton, 5, 2, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.saveButton = QPushButton(Dialog)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.saveButton, 5, 0, 1, 2)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 2)

        self.label_status = QLabel(Dialog)
        self.label_status.setObjectName(u"label_status")
        self.label_status.setStyleSheet(u"QLabel {\n"
"    font-family: \"Manrope\";\n"
"    font-size: 16px;\n"
"    font-weight: regular; \n"
"	background: none;\n"
"}")
        self.label_status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_status, 4, 0, 1, 3)

        QWidget.setTabOrder(self.nameInput, self.phoneInput)
        QWidget.setTabOrder(self.phoneInput, self.groupInput)
        QWidget.setTabOrder(self.groupInput, self.cancelButton)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Создать новый контакт", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043d\u043e\u0432\u044b\u0439 \u043a\u043e\u043d\u0442\u0430\u043a\u0442", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u0418\u043c\u044f:", None))
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u0413\u0440\u0443\u043f\u043f\u0430:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_status.setText("")
    # retranslateUi



class AddContactDialog(QDialog):
    def __init__(self, contact_manager, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.manager = contact_manager

        # Регулярное выражение: только цифры, длина от 11 до 12 символов
        phone_validator = QRegularExpressionValidator(QRegularExpression(r"^\d{11,12}$"))
        self.ui.phoneInput.setValidator(phone_validator)

        # Подключаем кнопку сохранения
        self.ui.saveButton.clicked.connect(self.save_contact)
        self.ui.cancelButton.clicked.connect(self.reject)

    def save_contact(self): # метод сохранения контактов
        name = self.ui.nameInput.text().strip()
        phone_number = self.ui.phoneInput.text().strip()
        group = self.ui.groupInput.text().strip() or None

        if not name or not phone_number:
            QMessageBox.warning(self, "Ошибка", "Введите имя и номер телефона!")
            return

        # форматирование перед сохранением
        formatted_number = self.manager.format_phone_number(phone_number)

        contact = Contact(formatted_number, name, group)

        if self.manager.add_contact(contact):
            msg = QMessageBox()
            msg.setWindowTitle("Успех")
            msg.setText("Контакт добавлен!")
            msg.setIcon(QMessageBox.Information)

            # Кастомизация шрифтов
            msg.setStyleSheet("""
                QMessageBox {
                    font-family: 'Manrope';
                    font-size: 14px;
                }
                QPushButton {
                    font-family: 'Mustica Pro';
                    font-size: 12px;
                    background-color: #007bff;
                    color: white;
                    border-radius: 5px;
                    padding: 5px 10px;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
            """)

            msg.exec()
            self.accept()  # Закрываем диалог в случае успеха
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Контакт с таким именем или номером уже существует!")
            msg.setIcon(QMessageBox.Warning)

            # Кастомизация шрифтов
            msg.setStyleSheet("""
                QMessageBox {
                    font-family: 'Manrope';
                    font-size: 14px;
                }
                QPushButton {
                    font-family: 'Mustica Pro';
                    font-size: 12px;
                    background-color: #d9534f;
                    color: white;
                    border-radius: 5px;
                    padding: 5px 10px;
                }
                QPushButton:hover {
                    background-color: #b52b27;
                }
            """)

            msg.exec()
