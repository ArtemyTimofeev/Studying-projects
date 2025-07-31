from PySide6.QtWidgets import QGraphicsLineItem, QGraphicsItem
from PySide6.QtGui import QPen
from PySide6.QtCore import QPointF, Signal, QObject


class DraggableArrow(QObject, QGraphicsLineItem):  # наследование от QObject и QGraphicsLineItem
    # этот класс отвечает за стрелочку в виде вертикальной палочки
    position_changed = Signal(float)

    def __init__(self, x, y, height, color, graphics_parent=None, qobject_parent=None):
        QObject.__init__(self, qobject_parent) # инициализация куобжект должна идти первой для наследования сигналов и слотов

        QGraphicsLineItem.__init__(self, 0, 0, 0, -height, graphics_parent)  # инициализация линии (синяя палочка от (0,0) до (0,хейгхт))

        self.setPos(x, y)  # устанавливаем палочку в у=0

        self.color = color # цвет
        self.original_height = height  # высота для масштабирования

        self.setPen(QPen(self.color, 2))  # Делаем линию немного толще для лучшей видимости

        self.setFlag(QGraphicsItem.ItemIsMovable) # объект двигаемый
        self.setFlag(QGraphicsItem.ItemSendsGeometryChanges) # изменяется геометрия
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache) # cache

        self.min_x = -float('inf')
        self.max_x = float('inf')

    def set_height(self, new_height):
        self.setLine(0, 0, 0, -new_height)  # рисуем линию напрямую с учетом знака new_height
        self.setPen(QPen(self.color, 2))  # ручка установлена

    def itemChange(self, change, value): # считывает изменения элемента для применения ограничений в целом
        if change == QGraphicsItem.ItemPositionChange:
            new_pos = value
            constrained_x = max(self.min_x, min(new_pos.x(), self.max_x)) # движение только по оси х!!!!!
            # Изменить положение объекта, если оно было изменено (принудительно)
            if abs(constrained_x - self.x()) > 0.1:  # допуск для сравнения float
                self.position_changed.emit(constrained_x)
            return QPointF(constrained_x, self.y())
        return super().itemChange(change, value)

    def set_x_constraints(self, min_x, max_x): # тут ограничения в координатах только по оси х
        self.min_x = min_x
        self.max_x = max_x
        # Принудительно применить ограничение, если текущая позиция выходит за пределы
        current_x = self.x()
        if not (self.min_x <= current_x <= self.max_x):
            constrained_x = max(self.min_x, min(current_x, self.max_x))
            self.setX(constrained_x)
            self.position_changed.emit(constrained_x)