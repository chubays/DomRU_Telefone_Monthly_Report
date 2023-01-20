from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout

import sys  # Только для доступа к аргументам командной строки


# Подкласс QMainWindow для настройки главного окна приложения
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.button_is_checked = True

        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)

        container = QWidget()
        container.setLayout(layout)

        self.setWindowTitle("Создание отчёта расходов за телефонию")
        # self.button = QPushButton("Press Me!")
        # self.button.setCheckable(True)
        # self.button.released.connect(self.the_button_was_released)
        # self.button.setChecked(self.button_is_checked)

        # Управляем размером окна
        # self.setFixedSize(QSize(800, 600))
        self.setMinimumSize(QSize(800, 600))
        self.setMaximumSize(QSize(1280, 1024))

        # Устанавливаем центральный виджет Window.
        # self.setCentralWidget(self.button)
        self.setCentralWidget(container)


    # def the_button_was_clicked(self):
    #     print("Clicked!")
    #
    # def the_button_was_toggled(self, checked):
    #     self.button_is_checked = checked
    #     print(self.button_is_checked)
    #
    # def the_button_was_released(self):
    #     self.button_is_checked = self.button.isChecked()
    #
    #     print(self.button_is_checked)


# Приложению нужен один (и только один) экземпляр QApplication.
# Передаём sys.argv, чтобы разрешить аргументы командной строки для приложения.
# Если не будете использовать аргументы командной строки, QApplication([]) тоже работает
app = QApplication([])

# Создаём виджет Qt — окно.
# window = QWidget()
# window = QPushButton("Push Me")
# window = QMainWindow()
window = MainWindow()
window.show()  # Важно: окно по умолчанию скрыто.

# Запускаем цикл событий.
app.exec()

# Приложение не доберётся сюда, пока вы не выйдете и цикл
# событий не остановится.
