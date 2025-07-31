from PySide6.QtWidgets import (
    QApplication, QMainWindow, QGraphicsView, QGraphicsScene,
    QVBoxLayout, QWidget, QLineEdit, QLabel, QFormLayout, QPushButton, QHBoxLayout,
    QGraphicsLineItem, QGraphicsTextItem, QGraphicsItem
)
from PySide6.QtGui import QPen, QColor, QBrush, QPainter
from PySide6.QtCore import Qt, QPointF, Signal, QObject, QRectF
from draggable_arrow import DraggableArrow

class OpticalScene(QGraphicsScene): # КЛАСС для отрисовки нашей системы координат, лучей и прочей оптической сцены
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSceneRect(-400, -300, 800, 600)  # размер сцены: x от -400 до 400, y от -300 до 300; суммарный масштаб
        self.focal_length = 0
        self.refractive_index = 1.5  # это показатель преломления, в принципе в будущем можно будет сделать так, чтобы пользователь его вводил внутри программки
        self.object_height = 50  # высота объекта

        self.init_optical_elements()

    def init_optical_elements(self): # инициализация оптической оси и линзы
        # Оптическая ось
        self.optical_axis = self.addLine(-self.sceneRect().width() / 2, 0, self.sceneRect().width() / 2, 0,
                                         QPen(Qt.black, 2))

        # Линза (простая вертикальная линия в x=0)
        self.lens_line = self.addLine(0, -100, 0, 100, QPen(Qt.darkGray, 3))

        # Отметки фокусных расстояний и их 2F-значений
        self.f_marks = []
        self.update_f_marks()

        # Объект (синяя палочка) - направлена вверх
        # Передаем None для graphics_parent и qobject_parent
        self.object_arrow = DraggableArrow(-200, 0, self.object_height, QColor(0, 0, 255))
        self.addItem(self.object_arrow)
        self.object_arrow.position_changed.connect(self.update_simulation)

        # Изображение (красная палочка)
        self.image_arrow = DraggableArrow(0, 0, self.object_height, QColor(255, 0, 0))
        self.image_arrow.setFlag(QGraphicsItem.ItemIsMovable, False)  # Изображение не должно быть перемещаемым
        self.addItem(self.image_arrow)
        self.image_arrow.setVisible(False)  # Скрыть, пока не рассчитается фокусное расстояние

        # Лучи
        self.rays = []
        self.update_simulation()  # Обновить симуляцию при инициализации

    def update_f_marks(self): # для обновления отметок ФР при изменении параметров пользователем
        for item in self.f_marks:
            self.removeItem(item)
        self.f_marks.clear()

        if self.focal_length == 0:
            return

        pen = QPen(Qt.black, 1)
        font = self.font()
        font.setPointSize(8)

        # F и -F отметки
        f_coords = [self.focal_length, -self.focal_length]  # f_coords[0] - F', f_coords[1] - F

        # F' (изображение)
        self.f_marks.append(self.addLine(f_coords[0], -5, f_coords[0], 5, pen))
        text_f_prime = QGraphicsTextItem("F'")  # F' - фокус на стороне изображения
        text_f_prime.setFont(font)
        text_f_prime.setPos(f_coords[0] - text_f_prime.boundingRect().width() / 2, 10)  # Ниже оси
        self.f_marks.append(text_f_prime)

        # F (объект)
        self.f_marks.append(self.addLine(f_coords[1], -5, f_coords[1], 5, pen))
        text_f = QGraphicsTextItem("F")  # F - фокус на стороне объекта
        text_f.setFont(font)
        text_f.setPos(f_coords[1] - text_f.boundingRect().width() / 2, 10)  # Ниже оси
        self.f_marks.append(text_f)

        # 2F' и -2F отметки
        twof_coords = [2 * self.focal_length, -2 * self.focal_length]

        # 2F'
        self.f_marks.append(self.addLine(twof_coords[0], -5, twof_coords[0], 5, pen))
        text_2f_prime = QGraphicsTextItem("2F'")
        text_2f_prime.setFont(font)
        text_2f_prime.setPos(twof_coords[0] - text_2f_prime.boundingRect().width() / 2, 10)
        self.f_marks.append(text_2f_prime)

        # 2F
        self.f_marks.append(self.addLine(twof_coords[1], -5, twof_coords[1], 5, pen))
        text_2f = QGraphicsTextItem("2F")
        text_2f.setFont(font)
        text_2f.setPos(twof_coords[1] - text_2f.boundingRect().width() / 2, 10)
        self.f_marks.append(text_2f)

    def set_focal_length(self, r1_str, r2_str): # считаем ФР на основе введённых радиусов кривизны
        try:
            r1 = float(r1_str) # вообще принимаем строку, но преобразуем её в число
            r2 = float(r2_str)

            if r1 == 0 or r2 == 0:
                self.focal_length = 0
                print("Ошибка: Радиусы не могут быть равны нулю.")
            else:
                # для двояковыпуклой линзы формула выглядит именно так.
                # НА БУДУЩЕЕ: можно будет допилить формулу, сделав для двояковогнутой -абс
                #             а также для полуплоских обнулять дроби с "бесконечными" радиусами
                self.focal_length = 1 / ((self.refractive_index - 1) * (1 / abs(r1) + 1 / abs(r2)))
                print(f"Рассчитанное фокусное расстояние: {self.focal_length:.2f}")

            self.update_f_marks()
            # Обновить ограничения для объекта после изменения f
            # Объекту разрешено быть между -3F и 0 (линзой)
            self.object_arrow.set_x_constraints(-3 * self.focal_length, 0)
            self.update_simulation()

        except ValueError:
            self.focal_length = 0
            self.update_f_marks()
            self.update_simulation()
            print("Неверный ввод для радиусов. Введите числовые значения.")

    def update_simulation(self): # обновляет красную стрелочку и трассировку лучей в зависимости от нового полученного местоположения
        # очищаем существующие лучи
        for ray in self.rays:
            self.removeItem(ray)
        self.rays.clear()
        self.image_arrow.setVisible(False)

        if self.focal_length == 0:
            return

        obj_x = self.object_arrow.x() # иксовая координата расположения палочки

        # применяем ограничения к позиции объекта (если он был перемещён за пределы)
        self.object_arrow.set_x_constraints(-3 * self.focal_length, 0)
        obj_x = self.object_arrow.x()  # получаем актуальную позицию после применения ограничений

        if obj_x == 0:  # отдельный случай, когда объект прямо на линзе
            self.image_arrow.setVisible(False)
            return

        # Расстояние до объекта (do) для формулы линзы, должно быть положительным.
        # Поскольку объект находится слева от линзы (x < 0), do = -obj_x.
        do = -obj_x

        # если объект находится в фокусе, изображение в бесконечности
        if abs(do - self.focal_length) < 0.1:  # небольшой допуск для сравнения с плавающей точкой
            self.image_arrow.setVisible(False)
            return

        try:
            # 1/di = 1/f - 1/do
            di_reciprocal = (1 / self.focal_length) - (1 / do)
            if di_reciprocal == 0:  # случай, когда изображение в бесконечности (если 1/f == 1/do)
                self.image_arrow.setVisible(False)
                return
            di = 1 / di_reciprocal
        except ZeroDivisionError:
            self.image_arrow.setVisible(False)  # тоже изображение в бесконечности (когда в принципе получаем 0)
            return

        magnification = -di / do # !!! знак увеличения определяет направление палочки !!!
        image_height = self.object_height * magnification

        # Установка положения и размера изображения
        image_x = di  # x-координата изображения
        self.image_arrow.setPos(image_x, 0)
        self.image_arrow.set_height(image_height)  # обновление высоты и ориентации палочки
        self.image_arrow.setVisible(True)

        obj_tip_y = self.object_height # игрековая координата вершины объекта

        # стили лучей
        incident_pen = QPen(Qt.darkMagenta, 1)  # Лучи до линзы
        refracted_pen = QPen(Qt.darkBlue, 1)  # Лучи после линзы
        dashed_refracted_pen = QPen(Qt.darkBlue, 1, Qt.DashLine)  # Пунктирные лучи для мнимого изображения

        # --- Трассировка трех основных лучей ---
        # Все Y-координаты передаются в addLine с инвертированным знаком для QGraphicsScene

        # Луч 1: Параллельный оптической оси, затем проходит через фокус изображения (F')
        # Падающий луч: от вершины объекта (obj_x, obj_tip_y) до линзы (0, obj_tip_y)
        ray1_incident = self.addLine(obj_x, -obj_tip_y, 0, -obj_tip_y, incident_pen)
        self.rays.append(ray1_incident)

        # Преломленный луч: от линзы (0, obj_tip_y) до вершины изображения (image_x, image_height)
        if di > 0:  # Действительное изображение (лучи сходятся)
            ray1_refracted = self.addLine(0, -obj_tip_y, image_x, -image_height, refracted_pen)
            self.rays.append(ray1_refracted)
        else:  # Мнимое изображение (лучи расходятся, их продолжение идет через F')
            # Определяем куда "реально" идёт луч (расходится)
            # Наклон луча (физический)
            m = (image_height - obj_tip_y) / (image_x - 0)
            # Отрезок, который реально выходит из линзы и идёт вправо
            ray1_refracted_solid = self.addLine(0, -obj_tip_y, self.sceneRect().right(),
                                                -(obj_tip_y + m * self.sceneRect().right()), refracted_pen)
            self.rays.append(ray1_refracted_solid)

            # Пунктирная часть (продолжение луча к мнимому изображению, влево от линзы)
            ray1_refracted_dashed = self.addLine(0, -obj_tip_y, image_x, -image_height, dashed_refracted_pen)
            self.rays.append(ray1_refracted_dashed)

        # Луч 2: Проходящий через оптический центр (0,0) - не преломляется
        # Идет от вершины объекта (obj_x, obj_tip_y) через (0,0) до вершины изображения (image_x, image_height)
        ray2_incident_refracted = self.addLine(obj_x, -obj_tip_y, image_x, -image_height, refracted_pen)
        self.rays.append(ray2_incident_refracted)

        # Луч 3: Проходящий через фокус объекта (F, т.е. -focal_length), затем параллельный оптической оси
        # Вычисляем y-координату (физическую), где луч попадает на линзу (x=0)

        # Y-координата на линзе для луча, идущего от вершины объекта через фокус F (-focal_length, 0)
        if abs(obj_x - (-self.focal_length)) < 0.1:  # Если объект находится очень близко к F
            ray3_lens_y = obj_tip_y  # Падающий луч уже параллелен оси
        else:
            # Наклон от вершины объекта (obj_x, obj_tip_y) до фокуса F (-self.focal_length, 0)
            slope_to_f = (0 - obj_tip_y) / (-self.focal_length - obj_x)
            # Y-координата, где луч попадает на линзу (x=0)
            ray3_lens_y = obj_tip_y + slope_to_f * (0 - obj_x)

        # Падающий луч: от вершины объекта до линзы
        ray3_incident = self.addLine(obj_x, -obj_tip_y, 0, -ray3_lens_y, incident_pen)  # Инвертируем Y
        self.rays.append(ray3_incident)

        # Преломленный луч: от линзы параллельно оптической оси.
        if di > 0:  # Действительное изображение
            # Луч идёт к точке сходимости.
            ray3_refracted = self.addLine(0, -ray3_lens_y, image_x, -image_height, refracted_pen)  # Инвертируем Y
            self.rays.append(ray3_refracted)
        else:  # Мнимое изображение
            # Действительная часть (параллельная от линзы)
            # Луч расходится, но его продолжение параллельно оси.
            # Отрисовываем реальную часть параллельно оси, от точки попадания на линзу (физическая y = ray3_lens_y).
            ray3_refracted_solid = self.addLine(0, -ray3_lens_y, self.sceneRect().right(), -ray3_lens_y,
                                                refracted_pen)  # Инвертируем Y
            self.rays.append(ray3_refracted_solid)

            # пунктирная часть (продолжение луча к мнимому изображению)
            ray3_refracted_dashed = self.addLine(0, -ray3_lens_y, image_x, -image_height,
                                                 dashed_refracted_pen)  # Инвертируем Y
            self.rays.append(ray3_refracted_dashed)

        self.update()  # принудительное обновление отрисовки сцены