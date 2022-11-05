import sys
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QMessageBox
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import Qt

import search_with_date
import separation_by_date_and_data
import separation_on_weeks
import separation_on_year
import iterator


class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()

        self.setGeometry(300, 250, 450, 350)
        self.setWindowTitle("Погода")

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Создание и выбор аннотаций")
        self.main_text.move(125, 10)
        self.main_text.adjustSize()

        self.folderpath_dataset = ""
        while self.folderpath_dataset == "":
            self.folderpath_dataset = QtWidgets.QFileDialog.getExistingDirectory(
                self, "Please select folder of dataset"
            )
        self.iterator_weather = iterator.Iterator("dataset.csv")

        self.botton1 = QtWidgets.QPushButton(self)
        self.botton1.setText("Разделение на года")
        self.botton1.setFixedWidth(300)
        self.botton1.move(70, 30)
        self.botton1.clicked.connect(self.year)

        self.botton2 = QtWidgets.QPushButton(self)
        self.botton2.setText("Разделение на недели")
        self.botton2.setFixedWidth(300)
        self.botton2.move(70, 60)
        self.botton2.clicked.connect(self.week)

        self.botton3 = QtWidgets.QPushButton(self)
        self.botton3.setText("Разделение на даты и данные")
        self.botton3.setFixedWidth(300)
        self.botton3.move(70, 90)
        self.botton3.clicked.connect(self.data_date)

        self.text = QtWidgets.QLabel(self)
        self.weather_text = QtWidgets.QLabel(self)
        self.btn_weather = QtWidgets.QPushButton(self)
        self.btn_weather.hide()
        self.btn_next = QtWidgets.QPushButton(self)
        self.btn_next.hide()
        self.dateEdit = QtWidgets.QDateEdit(self)
        self.dateEdit.hide()

    def hidden_text(self):
        self.text.setText("Введите дату дд/мм/гггг")
        self.text.move(135, 120)
        self.text.adjustSize()


       # self.calendar.setText("hjh")
        self.dateEdit.show()
        self.dateEdit.move(160,136)
        #self.dateEdit.setFixedWidth(200)


        self.weather_text.setText("Данные")
        self.weather_text.move(135, 230)
        self.weather_text.setFixedWidth(200)

        self.btn_weather.show()
        self.btn_weather.setText("Получить данные")
        self.btn_weather.setFixedWidth(200)
        self.btn_weather.move(120, 170)
        self.btn_weather.clicked.connect(self.data_of_weather)

        self.btn_next.show()
        self.btn_next.setText("Получить данные следующей даты")
        self.btn_next.setFixedWidth(300)
        self.btn_next.move(70, 200)
        self.btn_next.clicked.connect(self.next_date)

    def data_date(self) -> None:
        separation_by_date_and_data.main()
        self.flag = 1
        self.hidden_text()

    def week(self) -> None:
        separation_on_weeks.main()
        self.flag = 2
        self.hidden_text()

    def year(self) -> None:
        separation_on_year.main()
        self.flag = 3
        self.hidden_text()

    def data_of_weather(self) -> None:
        text = ''
        if self.flag == 1:
            text = search_with_date.search_in_data_and_date(self.dateEdit.dateTime().toString("dd-MM-yyyy"))
        else:
            if self.flag == 2:
                text = search_with_date.search_in_week_fast(search_with_date.day(self.dateEdit.dateTime().toString("dd-MM-yyyy")))
            else:
                text = search_with_date.search_in_year(search_with_date.day(self.dateEdit.dateTime().toString("dd-MM-yyyy")))
        self.weather_text.setText(text)
        self.weather_text.move(115, 230)
        self.weather_text.setFixedWidth(400)

    def next_date(self) -> None:
        print(self.iterator_weather.__next__())


def application():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
