import sys
from PySide6.QtWidgets import QApplication, QMainWindow # виджеты
from contact_manager import ContactManager # функционал из интерфейса командной строки
from ui_contact_manager import Ui_ContactManager  # главное окно
from add_contact_dialog import AddContactDialog  # окно добавления контакта
from show_all_contacts import ShowAllContactsWindow  # окно со списком контактов
from group_list import GroupListWindow  # окно со списком групп
from sure_exit import SureExitDialog  # окно подтверждения выхода

class ContactManagerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ContactManager()
        self.ui.setupUi(self)
        self.manager = ContactManager()

        # кнопки главного меню
        self.ui.btnCreateContact.clicked.connect(self.open_add_contact_dialog)
        self.ui.btnShowAllContacts.clicked.connect(self.open_show_contacts_window)
        self.ui.btnShowGroups.clicked.connect(self.open_group_list_window)
        self.ui.btnExit.clicked.connect(self.open_exit_dialog)

        self.show_contacts_window = None
        self.group_list_window = None

    def open_add_contact_dialog(self): # диалоговое окно "Новый контакт"
        dialog = AddContactDialog(self.manager, self)
        dialog.exec()

    def open_show_contacts_window(self): # диалоговое окно "Список контактов"
        if not self.show_contacts_window:
            self.show_contacts_window = ShowAllContactsWindow(self.manager, self)
        self.show_contacts_window.load_contacts()
        self.show_contacts_window.show()

    def open_group_list_window(self): # диалоговое окно "Список групп"
        if not self.group_list_window:
            self.group_list_window = GroupListWindow(self.manager, self)
        self.group_list_window.load_groups()
        self.group_list_window.show()

    def open_exit_dialog(self): # диалоговое окно подтверждения выхода
        exit_dialog = SureExitDialog(self)
        exit_dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ContactManagerApp()
    window.show()
    sys.exit(app.exec())
