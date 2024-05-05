from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import pandas as pd
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMainWindow
import datetime
import matplotlib.pyplot as plt
import pyqtgraph as pg
import numpy as np

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setObjectName("MainWindow")
        self.resize(1053, 800)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        #тут про tabWidget вкладки
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1051, 761))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        # тут про today
        self.today = QtWidgets.QWidget()
        self.today.setObjectName("today")
        # дата
        self.label_date = QtWidgets.QLabel(self.today)
        self.label_date.setGeometry(QtCore.QRect(0, 10, 309, 50))
        self.label_date.setObjectName("label_date")
        # тут должен быть индекс на цветном фоне
        self.label_value_index = QtWidgets.QLabel(self.today)
        self.label_value_index.setGeometry(QtCore.QRect(0, 50, 309, 50))
        self.label_value_index.setObjectName("label_value_index")
        self.label_value_index.setFont(QFont('Arial', 50))
        #про первую из надписей
        self.label_index = QtWidgets.QLabel(self.today)
        self.label_index.setGeometry(QtCore.QRect(0, 150, 309, 50))
        self.label_index.setObjectName("label_index")
        # 2 надпись
        self.label_recomendation = QtWidgets.QLabel(self.today)
        self.label_recomendation.setGeometry(QtCore.QRect(0, 200, 309, 50))
        self.label_recomendation.setObjectName("label_recomendation")
        # radiobutton
        self.verticalLayoutWidget = QtWidgets.QWidget(self.today)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 300, 221, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radio_co = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_co.setObjectName("radio_co")
        self.radio_co.setChecked(True)
        self.verticalLayout.addWidget(self.radio_co)
        self.radio_o = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_o.setObjectName("radio_o")
        self.verticalLayout.addWidget(self.radio_o)
        self.radio_no2 = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radio_no2.setObjectName("radio_no2")
        self.verticalLayout.addWidget(self.radio_no2)
        # 3 надпись
        self.label_concetration = QtWidgets.QLabel(self.today)
        self.label_concetration.setGeometry(QtCore.QRect(0, 510, 551, 81))
        self.label_concetration.setObjectName("label_concetration")
        self.tabWidget.addTab(self.today, "") # как я понял сначала прописываем что там должно быть, а потом типо добавляем только
        # вкладка history
        self.history = QtWidgets.QWidget()
        self.history.setObjectName("history")
        # Группа кнопок горизонтальных
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.history)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1021, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # первая кнопка
        self.pushButton_yesterday6 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_yesterday6.setObjectName("pushButton_yesterday6")
        self.horizontalLayout.addWidget(self.pushButton_yesterday6)
        # вторая кнопка
        self.pushButton_yesterday5 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_yesterday5.setObjectName("pushButton_yesterday5")
        self.horizontalLayout.addWidget(self.pushButton_yesterday5)
        # 3
        self.pushButton_yesterday4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_yesterday4.setObjectName("pushButton_yesterday4")
        self.horizontalLayout.addWidget(self.pushButton_yesterday4)
        # 4
        self.pushButton_yesterday3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_yesterday3.setObjectName("pushButton_yesterday3")
        self.horizontalLayout.addWidget(self.pushButton_yesterday3)
        # 5
        self.pushButton_yesterday2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_yesterday2.setObjectName("pushButton_yesterday2")
        self.horizontalLayout.addWidget(self.pushButton_yesterday2)
        # 6
        self.pushButton_yesterday1 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_yesterday1.setObjectName("pushButton_yesterday1")
        self.horizontalLayout.addWidget(self.pushButton_yesterday1)
        # 7 - сегодня
        self.pushButton_today = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_today.setObjectName("pushButton_today")
        self.horizontalLayout.addWidget(self.pushButton_today)
        # опять тот блок что на первой странице
        self.label_value_index2 = QtWidgets.QLabel(self.history)
        self.label_value_index2.setGeometry(QtCore.QRect(0, 70, 309, 50))
        self.label_value_index2.setObjectName("label_value_index2")
        self.label_value_index2.setFont(QFont('Arial', 50))
        self.label_index_2 = QtWidgets.QLabel(self.history)
        self.label_index_2.setGeometry(QtCore.QRect(0, 170, 309, 50))
        self.label_index_2.setObjectName("label_index_2")
        self.label_recomendation_2 = QtWidgets.QLabel(self.history)
        self.label_recomendation_2.setGeometry(QtCore.QRect(0, 220, 309, 50))
        self.label_recomendation_2.setObjectName("label_recomendation_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.history)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 320, 221, 221))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radio_co_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radio_co_2.setObjectName("radio_co_2")
        self.radio_co_2.setChecked(True)
        self.verticalLayout_2.addWidget(self.radio_co_2)
        self.radio_o_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radio_o_2.setObjectName("radio_o_2")
        self.verticalLayout_2.addWidget(self.radio_o_2)
        self.radio_no2_2 = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radio_no2_2.setObjectName("radio_no2_2")
        self.verticalLayout_2.addWidget(self.radio_no2_2)
        # задается промежуток
        self.dateEdit = QtWidgets.QDateEdit(self.history)
        self.dateEdit.setGeometry(QtCore.QRect(250, 530, 181, 51))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setCalendarPopup(True)
        self.first_day = QtWidgets.QLabel(self.history)
        self.first_day.setGeometry(QtCore.QRect(0, 530, 251, 50))
        self.first_day.setObjectName("first_day")
        self.finish_day = QtWidgets.QLabel(self.history)
        self.finish_day.setGeometry(QtCore.QRect(0, 610, 251, 50))
        self.finish_day.setObjectName("finish_day")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.history)
        self.dateEdit_2.setGeometry(QtCore.QRect(250, 610, 181, 51))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.dateEdit_2.setCalendarPopup(True)
        """self.layout = QtWidgets.QVBoxLayout(self.history)
        self.plot_container = QtWidgets.QWidget(self.history)
        self.plot_container.setMinimumSize(QtCore.QSize(0, 200))
        self.layout.addWidget(self.plot_container)

        # График
        self.plot_widget = pg.PlotWidget(self.plot_container)
        self.plot_widget.setFixedWidth(20)  # Установка ширины графика
        self.plot_widget.setFixedHeight(20)
        self.plot_widget.setGeometry(QtCore.QRect(250, 610, 181, 51))
        self.layout_plot = QtWidgets.QVBoxLayout(self.plot_container)
        self.layout_plot.addWidget(self.plot_widget)

        # Тестовые данные для графика
        x = np.linspace(0, 10, 100)
        y = np.sin(x)

        # Построение графика
        self.plot_widget.plot(x, y, pen='b')"""

        # скрол
        self.verticalScrollBar = QtWidgets.QScrollBar(self.history)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1030, 0, 16, 721))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.graphicsView = QtWidgets.QGraphicsView(self.history)
        self.graphicsView.setGeometry(QtCore.QRect(10, 690, 256, 192))
        self.graphicsView.setObjectName("graphicsView")
        self.tabWidget.addTab(self.history, "")# опять добавление
        # следующая вкладка, но пустая пока
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "")
        self.setCentralWidget(self.centralwidget)
        # меню
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1053, 37))
        # настройки меню
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(50)
        self.menubar.setFont(font)
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setGeometry(QtCore.QRect(270, 164, 159, 78))
        self.menu.setObjectName("menu")
        self.setMenuBar(self.menubar)
        self.exit = QtWidgets.QAction(self)
        self.exit.setObjectName("exit")
        self.exit.triggered.connect(self.close)
        self.menu.addAction(self.exit)
        self.menubar.addAction(self.menu.menuAction())


        date_array = []
        main_date = '2005-04-04'
        formal_main_date = datetime.datetime.strptime(main_date, '%Y-%m-%d')
        for i in range(7):
            date_array.append((formal_main_date + datetime.timedelta(days=-6 + i)).date())
        hour = 18
        two_week_day = (formal_main_date + datetime.timedelta(days=-14)).date()
        self.dateEdit.setMinimumDate(QtCore.QDate(2004, 3, 10))
        self.dateEdit.setMaximumDate(QtCore.QDate(2005, 4, 3))
        self.dateEdit_2.setMinimumDate(QtCore.QDate(2004, 3, 10))
        self.dateEdit_2.setMaximumDate(QtCore.QDate(2005, 4, 3))
        initial_date1 = QtCore.QDate(two_week_day.year, two_week_day.month, two_week_day.day)
        self.dateEdit.setDate(initial_date1)
        initial_date2 = QtCore.QDate(date_array[5].year, date_array[5].month, date_array[5].day)
        self.dateEdit_2.setDate(initial_date2)
        selected_date1 = self.dateEdit.date()
        selected_date2 = self.dateEdit_2.date()
        self.radio_co.clicked.connect(lambda: self.show_label_with_radio(main_date, hour))
        self.radio_o.clicked.connect(lambda: self.show_label_with_radio(main_date, hour))
        self.radio_no2.clicked.connect(lambda: self.show_label_with_radio(main_date, hour))
        self.radio_co_2.clicked.connect(lambda: self.show_label_with_radio(selected_date1, selected_date2))
        self.radio_o_2.clicked.connect(lambda: self.show_label_with_radio(selected_date1, selected_date2))
        self.radio_no2_2.clicked.connect(lambda: self.show_label_with_radio(selected_date1, selected_date2))
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.loaded_data = None
        self.load_data()
        self.today_tab(main_date, hour)
        self.history_tab(date_array, hour)
        self.pushButton_today.setCheckable(True)
        self.pushButton_yesterday6.clicked.connect(lambda: self.show_page_with_push(str(date_array[0]), 24, self.pushButton_today))
        self.pushButton_yesterday5.clicked.connect(lambda: self.show_page_with_push(str(date_array[1]), 24, self.pushButton_today))
        self.pushButton_yesterday4.clicked.connect(lambda: self.show_page_with_push(str(date_array[2]), 24, self.pushButton_today))
        self.pushButton_yesterday3.clicked.connect(lambda: self.show_page_with_push(str(date_array[3]), 24, self.pushButton_today))
        self.pushButton_yesterday2.clicked.connect(lambda: self.show_page_with_push(str(date_array[4]), 24, self.pushButton_today))
        self.pushButton_yesterday1.clicked.connect(lambda: self.show_page_with_push(str(date_array[5]), 24, self.pushButton_today))
        self.pushButton_today.clicked.connect(lambda: self.show_page_with_push(str(date_array[6]), hour, self.pushButton_today, False))
        self.pushButton_today.click()





    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "AirQuality"))
        self.radio_co.setText( "Угарный газ")
        self.radio_o.setText(_translate("MainWindow", "Озон"))
        self.radio_no2.setText(_translate("MainWindow", "Диоксид азота"))
        self.label_index_2.setText(_translate("MainWindow", "Индекс качества воздуха"))
        self.radio_co_2.setText(_translate("MainWindow", "Угарный газ"))
        self.radio_o_2.setText(_translate("MainWindow", "Озон"))
        self.radio_no2_2.setText(_translate("MainWindow", "Диоксид азота"))
        self.first_day.setText(_translate("MainWindow", "Начало промежутка"))
        self.finish_day.setText(_translate("MainWindow", "Конец промежутка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.today), _translate("MainWindow", "Состояние на сегодня"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.history), _translate("MainWindow", "Историческая сводка"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Расчёт"))
        self.menu.setTitle(_translate("MainWindow", "Меню"))
        self.exit.setText(_translate("MainWindow", "Выход"))


    def load_data(self):
        # Здесь можно загрузить данные из файла или другого источника
        self.loaded_data = pd.read_csv("AirQuality_processed.csv")
        #print(self.loaded_data)

    def count_aqi(self, date, hour):
        if self.loaded_data is not None:
            data_array = self.loaded_data.values
            CO = []
            O3 = []
            NO2 = []
            last_index = -1
            while(len(CO) < 8):
                for i in range(len(data_array)):
                    if data_array[i][0] == date and data_array[i][4] <= hour:
                        last_index = i
                        CO.append(data_array[i][5]/100)
                        O3.append(data_array[i][9]/10)
                        NO2.append(data_array[i][8]/10)
                    elif len(CO)>0:
                        break
                if len(CO) < 8 and last_index!=-1:
                    for i in range(8-len(CO)):
                        CO.append(data_array[last_index-len(CO)][5] / 100)
                        O3.append(data_array[last_index-len(O3)][9] / 10)
                        NO2.append(data_array[last_index-len(NO2)][8] / 10)
                elif last_index == -1:
                    date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
                    previous_date = (date_obj + datetime.timedelta(days=-1)).date()
                    date = str(previous_date)
                    hour == 23
            co = sum(CO)/len(CO)
            o3 = sum(O3) / len(O3)
            no2 = sum(NO2) / len(NO2)
            if o3 <= 54:
                o3_aqi = 50/54*o3
            elif o3 >= 55 and o3 <= 70:
                o3_aqi = (100 - 51) / (70 - 55) * (o3-55)+51
            elif o3 >= 71 and o3 <= 85:
                o3_aqi = (150 - 101) / (85 - 71) * (o3 - 71) + 101
            elif o3 >= 86 and o3 <= 105:
                o3_aqi = (200 - 151) / (105 - 86) * (o3 - 86) + 151
            elif o3 >= 106 and o3 <= 212:
                o3_aqi = (300 - 201) / (212 - 106) * (o3 - 106) + 201
            if co <= 4.4:
                co_aqi = 50/4.4*co
            elif co >= 4.5 and co <= 9.4:
                co_aqi = (100 - 51) / (9.4 - 4.5) * (co-4.5)+51
            elif co >= 9.5 and co <= 12.4:
                co_aqi = (150 - 101) / (12.4 - 9.5) * (co - 9.5) + 101
            elif co >= 12.5 and co <= 15.4:
                co_aqi = (200 - 151) / (15.4 - 12.5) * (co - 12.5) + 151
            elif co >= 15.5 and co <= 30.4:
                co_aqi = (200 - 151) / (30.4 - 15.5) * (co - 15.5) + 151
            if no2 <= 53:
                no2_aqi = 50/53*no2
            elif no2 >= 54 and no2 <= 100:
                no2_aqi = (100 - 51) / (100 - 54) * (no2-54)+51
            elif no2 >= 101 and no2 <= 360:
                no2_aqi = (150 - 101) / (360 - 101) * (no2 - 101) + 101
            elif no2 >= 361 and no2 <= 649:
                no2_aqi = (200 - 151) / (649 - 361) * (no2 - 361) + 151
            if co_aqi <= o3_aqi >= no2_aqi:
                aqi = o3_aqi
            elif o3_aqi <= co_aqi >= no2_aqi:
                aqi = co_aqi
            elif o3_aqi <= no2_aqi >= co_aqi:
                aqi = no2_aqi
            return [aqi, co, o3, no2]




    def today_tab(self, date, hour):
        info_today = self.count_aqi(date, hour)
        date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
        date_obj = date_obj.strftime('%d.%m.%Y')
        self.label_date.setText(f"Сегодня, {date_obj}, состояние воздуха на {hour}:00")
        self.label_date.adjustSize()
        self.label_value_index.setText(f"{int(info_today[0])}")
        self.label_value_index.adjustSize()
        if info_today[0] <= 50:
            self.label_value_index.setStyleSheet("background-color: lightgreen")
            self.label_recomendation.setText("Никаких последствий для здоровья. Каждый может продолжать свои занятия\nна улице в обычном режиме.")
        elif info_today[0] >= 51 and info_today[0] <= 100:
            self.label_value_index.setStyleSheet("background-color: #fdff72")
            self.label_recomendation.setText("Некоторые загрязняющие вещества могут незначительно влиять на немногих\nгиперчувствительных людей. Таким людям следует проводить на улице\nменьше времени.")
        elif info_today[0] >= 101 and info_today[0] <= 150:
            self.label_value_index.setStyleSheet("background-color: orange")
            self.label_recomendation.setText(
                "Здоровые люди могут испытывать легкое раздражение, а чувствительные люди будут\nподвержены воздействию в большей степени. Детям, пожилым людям и лицам с\nзаболеваниями органов дыхания или сердца следует меньше времени\nпроводить на улице.")
        elif info_today[0] >= 151 and info_today[0] <= 200:
            self.label_value_index.setStyleSheet("background-color: red")
            self.label_recomendation.setText(
                "Чувствительные люди могут быть подвержены серьезным заболеваниям. У здоровых\nлюдей могут быть затронуты сердце и дыхательная система. Детям, пожилым\nлюдям и лицам с заболеваниями органов дыхания или сердца следует избегать\nдлительного нахождения на улице.")
        elif info_today[0] >= 201 and info_today[0] <= 300:
            self.label_value_index.setStyleSheet("background-color: #4B0082")
            self.label_recomendation.setText(
                "Люди с респираторными или сердечными заболеваниями значительно пострадают\nи будут испытывать снижение выносливости при физических нагрузках. Детям, пожилым\nлюдям и лицам с заболеваниями сердца или легких следует оставаться в помещении.")
        elif info_today[0] >= 301:
            self.label_value_index.setStyleSheet("background-color: #800000")
            self.label_recomendation.setText(
                "У здоровых людей снижается выносливость при физических нагрузках, а также\nмогут проявляться заметно выраженные симптомы болезней. Детям, пожилым и\nбольным людям следует оставаться в помещении и избегать физических нагрузок.")
        self.label_recomendation.adjustSize()
        self.label_index.setText(f"Индекс качества воздуха")
        self.label_concetration.setText(f"Концетрация угарного газа в воздухе составляет {round(info_today[1], 2)} ppm")
        self.label_concetration.adjustSize()

    def show_label_with_radio(self, date, hour):
        info_today = self.count_aqi(date, hour)
        sender = self.sender()
        if sender == self.radio_co:
            self.label_concetration.setText(f"Концетрация угарного газа в воздухе составляет {round(info_today[1], 2)} ppm")
        elif sender == self.radio_o:
            self.label_concetration.setText(f"Концетрация озона в воздухе составляет {round(info_today[2], 2)} ppb")
        elif sender == self.radio_no2:
            self.label_concetration.setText(f"Концетрация двуокиси азота в воздухе составляет {round(info_today[3], 2)} ppb")
        self.label_concetration.adjustSize()

    def show_label_with_radio2(self, first_date, finish_date):
        info = []
        x = []
        y = []
        if (first_date > finish_date):
            print("Error")
        delta = finish_date-first_date
        for i in range(delta.days):
            current_date = (first_date + datetime.timedelta(days=i)).date()
            x.append(current_date)
            info[i] = self.count_aqi(str(current_date), 24)
        sender = self.sender()
        if sender == self.radio_co_2:
            for i in range(len(info)):
                y.append(info[i][1])
            plt.ylabel('Концентрация CO, ppm')
        elif sender == self.radio_o_2:
            pass
        elif sender == self.radio_no2_2:
            pass
        plt.plot(x, y, marker='o')  # Построение графика с маркерами точек
        plt.xlabel('Дата')  # Подпись оси x
        plt.ylabel('Значение')  # Подпись оси y
        plt.xticks(rotation=45)  # Поворот подписей дат для лучшей видимости
        plt.grid(True)  # Включение сетки на графике
        plt.tight_layout()  # Автоматическая расстановка элементов для лучшего отображения
        plt.show()

    def show_page_with_push(self, date, hour, button, flag = True):
        if (flag):
            button.setCheckable(False)
            button.update()
        info_today = self.count_aqi(str(date), hour)
        self.label_value_index2.setText(f"{int(info_today[0])}")
        self.label_value_index2.adjustSize()
        if info_today[0] <= 50:
            self.label_value_index2.setStyleSheet("background-color: lightgreen")
            self.label_recomendation_2.setText(
                "Никаких последствий для здоровья. Каждый может продолжать свои занятия\nна улице в обычном режиме.")
        elif info_today[0] >= 51 and info_today[0] <= 100:
            self.label_value_index2.setStyleSheet("background-color: #fdff72")
            self.label_recomendation_2.setText(
                "Некоторые загрязняющие вещества могут незначительно влиять на немногих\nгиперчувствительных людей. Таким людям следует проводить на улице\nменьше времени.")
        elif info_today[0] >= 101 and info_today[0] <= 150:
            self.label_value_index2.setStyleSheet("background-color: orange")
            self.label_recomendation_2.setText(
                "Здоровые люди могут испытывать легкое раздражение, а чувствительные люди будут\nподвержены воздействию в большей степени. Детям, пожилым людям и лицам с\nзаболеваниями органов дыхания или сердца следует меньше времени\nпроводить на улице.")
        elif info_today[0] >= 151 and info_today[0] <= 200:
            self.label_value_index2.setStyleSheet("background-color: red")
            self.label_recomendation_2.setText(
                "Чувствительные люди могут быть подвержены серьезным заболеваниям. У здоровых\nлюдей могут быть затронуты сердце и дыхательная система. Детям, пожилым\nлюдям и лицам с заболеваниями органов дыхания или сердца следует избегать\nдлительного нахождения на улице.")
        elif info_today[0] >= 201 and info_today[0] <= 300:
            self.label_value_index2.setStyleSheet("background-color: #4B0082")
            self.label_recomendation_2.setText(
                "Люди с респираторными или сердечными заболеваниями значительно пострадают\nи будут испытывать снижение выносливости при физических нагрузках. Детям, пожилым\nлюдям и лицам с заболеваниями сердца или легких следует оставаться в помещении.")
        elif info_today[0] >= 301:
            self.label_value_index2.setStyleSheet("background-color: #800000")
            self.label_recomendation_2.setText(
                "У здоровых людей снижается выносливость при физических нагрузках, а также\nмогут проявляться заметно выраженные симптомы болезней. Детям, пожилым и\nбольным людям следует оставаться в помещении и избегать физических нагрузок.")
        self.label_recomendation_2.adjustSize()
        self.label_index_2.setText(f"Индекс качества воздуха")



    def history_tab(self, date_array, hour):
        date_array_processed = []
        for i in range(len(date_array)):
            date_array_processed.append(date_array[i].strftime('%d.%m.%Y'))
        self.pushButton_yesterday6.setText(str(date_array_processed[0]))
        self.pushButton_yesterday5.setText(str(date_array_processed[1]))
        self.pushButton_yesterday4.setText(str(date_array_processed[2]))
        self.pushButton_yesterday3.setText(str(date_array_processed[3]))
        self.pushButton_yesterday2.setText(str(date_array_processed[4]))
        self.pushButton_yesterday1.setText(str(date_array_processed[5]))
        self.pushButton_today.setText(str(date_array_processed[6]))



Stylesheet = '''
QWidget {
    font-size: 25px;
}
QPushButton:checked {
    border: 2px solid #09009B;
}
QPushButton:focus {
    border: 2px solid #09009B;
}
#label_value_index, #label_value_index2 {
    font-size: 70px;
}
'''



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(Stylesheet)
    window = MainWindow()
    window.show()
    app.exec_()
