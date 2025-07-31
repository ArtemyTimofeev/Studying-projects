import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QGraphicsView,
    QVBoxLayout, QWidget, QLineEdit, QFormLayout, QPushButton, QHBoxLayout,
)
from PySide6.QtGui import QPainter
from optical_scene import OpticalScene

class LensSimulator(QMainWindow):
    """
    Основное окно приложения PySide6 для симулятора линзы.
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Симулятор двояковыпуклой линзы")
        self.setGeometry(100, 100, 1000, 600)  # размеры окна

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)
        self.central_widget.setStyleSheet(u"QWidget {\n"
                                    "    font-family: \"Manrope\";\n"
                                    "    font-size: 16px;\n"
                                    "    font-weight: regular; \n"
                                    "	background: none;\n"
                                    "}")

        # Поля ввода для радиусов
        self.input_layout = QFormLayout()
        self.r1_input = QLineEdit("100")  # Значение по умолчанию
        self.r2_input = QLineEdit("100")  # Значение по умолчанию
        self.r1_input.setPlaceholderText("Радиус R1 (например, 100)")
        self.r2_input.setPlaceholderText("Радиус R2 (например, 100)")


        self.input_layout.addRow("Радиус кривизны R1:", self.r1_input)
        self.input_layout.addRow("Радиус кривизны R2:", self.r2_input)
        self.r1_input.setStyleSheet(u"QLineEdit {\n"
                                      "    font-family: \"Manrope\";\n"
                                      "    font-size: 16px;\n"
                                      "    font-weight: regular; \n"
                                      "	background: none;\n"
                                      "}")
        self.r2_input.setStyleSheet(u"QLineEdit {\n"
                                    "    font-family: \"Manrope\";\n"
                                    "    font-size: 16px;\n"
                                    "    font-weight: regular; \n"
                                    "	background: none;\n"
                                    "}")

        self.calculate_button = QPushButton("Рассчитать и обновить")
        self.calculate_button.setStyleSheet(u"QPushButton {\n"
                                      "    font-family: \"Manrope\";\n"
                                      "    font-size: 16px;\n"
                                      "    font-weight: regular; \n"
                                      "	background: none;\n"
                                      "}")
        self.calculate_button.clicked.connect(self.calculate_focal_length)

        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.calculate_button)
        button_layout.addStretch()

        self.main_layout.addLayout(self.input_layout)
        self.main_layout.addLayout(button_layout)

        # Виджет для отображения графики
        self.scene = OpticalScene()
        self.view = QGraphicsView(self.scene)
        self.view.setRenderHint(QPainter.Antialiasing)  # сглаживание для плавных линий
        self.main_layout.addWidget(self.view)

        # Начальный расчет при запуске программы
        self.calculate_focal_length()

    def calculate_focal_length(self):
        """Вызывает метод сцены для расчета фокусного расстояния и обновления симуляции."""
        self.scene.set_focal_length(self.r1_input.text(), self.r2_input.text())


if __name__ == "__main__":
    app = QApplication()
    window = LensSimulator()
    window.show()
    sys.exit(app.exec())