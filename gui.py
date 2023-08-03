# -*- coding: utf-8 -*-
import sys


from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QAbstractTableModel, QModelIndex, QStringListModel)
"""from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
"""
from PySide6.QtWidgets import (QApplication, QDateEdit, QGroupBox, QHBoxLayout,
                               QHeaderView, QLabel, QMainWindow, QPushButton,
                               QSizePolicy, QStatusBar, QTabWidget, QTableWidget,
                               QTableWidgetItem, QVBoxLayout, QWidget, QTableView, QGridLayout, QLineEdit, QFileDialog,
                               QListView, QLayout)


class PandasModel(QAbstractTableModel):
    """A model to interface a Qt view with pandas dataframe """

    def __init__(self, dataframe: pd.DataFrame, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._dataframe = dataframe

    def rowCount(self, parent=QModelIndex()) -> int:
        """ Override method from QAbstractTableModel

        Return row count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe)

        return 0

    def columnCount(self, parent=QModelIndex()) -> int:
        """Override method from QAbstractTableModel

        Return column count of the pandas DataFrame
        """
        if parent == QModelIndex():
            return len(self._dataframe.columns)
        return 0

    def data(self, index: QModelIndex, role=Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return data cell from the pandas DataFrame
        """
        if not index.isValid():
            return None

        if role == Qt.DisplayRole:
            return str(self._dataframe.iloc[index.row(), index.column()])

        return None

    def headerData(self, section: int, orientation: Qt.Orientation, role: Qt.ItemDataRole):
        """Override method from QAbstractTableModel

        Return dataframe index as vertical header data and columns as horizontal header data.
        """
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._dataframe.columns[section])

            if orientation == Qt.Vertical:
                return str(self._dataframe.index[section])

        return None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_read = QPushButton(self.groupBox)
        self.btn_read.setObjectName(u"btn_read")

        self.verticalLayout_2.addWidget(self.btn_read)

        self.groupBox_2 = QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.start_date = QDateEdit(self.groupBox_2)
        self.start_date.setObjectName(u"start_date")
        self.start_date.setEnabled(False)
        self.start_date.setCalendarPopup(True)

        self.verticalLayout_3.addWidget(self.start_date)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.end_date = QDateEdit(self.groupBox_2)
        self.end_date.setObjectName(u"end_date")
        self.end_date.setEnabled(False)
        self.end_date.setCalendarPopup(True)

        self.btn_request = QPushButton(self.groupBox_2)
        self.btn_request.setObjectName(u"btn_request")


        self.verticalLayout_3.addWidget(self.end_date)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.btn_calculate = QPushButton(self.groupBox)
        self.btn_calculate.setObjectName(u"btn_calculate")
        self.btn_calculate.setEnabled(False)

        self.verticalLayout_2.addWidget(self.btn_calculate)

        self.btn_save_report = QPushButton(self.groupBox)
        self.btn_save_report.setObjectName(u"btn_save_report")
        self.btn_save_report.setEnabled(False)

        self.verticalLayout_2.addWidget(self.btn_save_report)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_2.addWidget(self.label_3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)


        self.gridLayout.addWidget(self.groupBox, 0, 3, 1, 1)

        self.groupBox_3 = QGroupBox(self.tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_5)

        self.le_subscription = QLineEdit(self.groupBox_3)
        self.le_subscription.setObjectName(u"le_subscription")
        self.le_subscription.setClearButtonEnabled(False)

        self.horizontalLayout.addWidget(self.le_subscription)

        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_6)

        self.le_personal = QLineEdit(self.groupBox_3)
        self.le_personal.setObjectName(u"le_personal")

        self.horizontalLayout.addWidget(self.le_personal)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.le_divisions_cost = QLineEdit(self.groupBox_3)
        self.le_divisions_cost.setObjectName(u"le_divisions_cost")

        self.horizontalLayout.addWidget(self.le_divisions_cost)

        self.label_8 = QLabel(self.groupBox_3)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.le_minuts = QLineEdit(self.groupBox_3)
        self.le_minuts.setObjectName(u"le_minuts")

        self.horizontalLayout.addWidget(self.le_minuts)

        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setEnabled(True)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(True)

        self.horizontalLayout.addWidget(self.label_9)

        self.le_cost_for_number = QLineEdit(self.groupBox_3)
        self.le_cost_for_number.setObjectName(u"le_cost_for_number")

        self.horizontalLayout.addWidget(self.le_cost_for_number)

        self.btn_from_invoice = QPushButton(self.groupBox_3)
        self.btn_from_invoice.setObjectName(u"btn_from_invoice")

        self.horizontalLayout.addWidget(self.btn_from_invoice)


        self.gridLayout.addWidget(self.groupBox_3, 1, 1, 1, 3)

        self.tableView = QTableView(self.tab)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 0, 2, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_2 = QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox_4 = QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetMaximumSize)
        self.lv_divisions = QListView(self.groupBox_4)
        self.lv_divisions.setObjectName(u"lv_divisions")

        self.verticalLayout_4.addWidget(self.lv_divisions)


        self.gridLayout_2.addWidget(self.groupBox_4, 0, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.tab_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_5.addWidget(self.label_10)

        self.tw_phones = QTableView(self.groupBox_5)
        self.tw_phones.setObjectName(u"tw_phones")

        self.verticalLayout_5.addWidget(self.tw_phones)


        self.horizontalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_20 = QLabel(self.groupBox_5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_20)

        self.le_name = QLineEdit(self.groupBox_5)
        self.le_name.setObjectName(u"le_name")

        self.verticalLayout_6.addWidget(self.le_name)

        self.label_21 = QLabel(self.groupBox_5)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_21)

        self.lineEdit_5 = QLineEdit(self.groupBox_5)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setEnabled(False)

        self.verticalLayout_6.addWidget(self.lineEdit_5)

        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_11)

        self.le_divisions = QLineEdit(self.groupBox_5)
        self.le_divisions.setObjectName(u"le_divisions")

        self.verticalLayout_6.addWidget(self.le_divisions)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)
        self.label_12.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_12)

        self.le_personals = QLineEdit(self.groupBox_5)
        self.le_personals.setObjectName(u"le_personals")

        self.verticalLayout_6.addWidget(self.le_personals)

        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_6.addWidget(self.label_17)

        self.btn_save_divisions = QPushButton(self.groupBox_5)
        self.btn_save_divisions.setObjectName(u"btn_save_divisions")

        self.verticalLayout_6.addWidget(self.btn_save_divisions)

        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_6.addWidget(self.label_18)

        self.label_19 = QLabel(self.groupBox_5)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_6.addWidget(self.label_19)

        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_6.addWidget(self.label_16)

        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_6.addWidget(self.label_15)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_6.addWidget(self.label_14)

        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_6.addWidget(self.label_13)


        self.horizontalLayout_2.addLayout(self.verticalLayout_6)


        self.gridLayout_2.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0438\u0438 \u0414\u043e\u043c\u0420\u0443", None))
        self.groupBox.setTitle("")
        self.btn_read.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0447\u0438\u0442\u0430\u0442\u044c \u0444\u0430\u0439\u043b\u044b", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0438\u043e\u0434 \u043e\u0442\u0447\u0451\u0442\u0430", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043d\u0430\u0447\u0430\u043b\u0430", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u0442\u0430 \u043e\u043a\u043e\u043d\u0447\u0430\u043d\u0438\u044f", None))
        self.btn_calculate.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0444\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u043e\u0442\u0447\u0451\u0442", None))
        self.btn_save_report.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043e\u0442\u0447\u0451\u0442", None))
        self.label_3.setText("")
        self.label_4.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0445\u043e\u0434\u044b", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0431\u043e\u043d\u0435\u043d\u0442\u0441\u043a\u0430\u044f \u043f\u043b\u0430\u0442\u0430", None))
        self.le_subscription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"3500", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043d\u043e\u043c\u0435\u0440\u0430", None))
        self.le_personal.setPlaceholderText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b\u044b", None))
        self.le_divisions_cost.setPlaceholderText(QCoreApplication.translate("MainWindow", u"900", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0443\u0442\u044b", None))
        self.le_minuts.setPlaceholderText(QCoreApplication.translate("MainWindow", u"23500", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0435\u043d\u0430 \u0437\u0430 \u043d\u043e\u043c\u0435\u0440", None))
        self.le_cost_for_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"160", None))
        self.btn_from_invoice.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u043e\u043b\u043d\u0438\u0442\u044c \u0438\u0437 \u0441\u0447\u0451\u0442\u0430", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0451\u0442", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0434\u0435\u043b\u044b", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u0435\u0444\u043e\u043d\u044b \u043e\u0442\u0434\u0435\u043b\u0430", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043e\u0442\u0434\u0435\u043b\u043e\u0432", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432", None))
        self.label_17.setText("")
        self.btn_save_divisions.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0438\u0437\u043c\u0435\u043d\u0435\u043d\u0438\u044f", None))
        self.label_18.setText("")
        self.label_19.setText("")
        self.label_16.setText("")
        self.label_15.setText("")
        self.label_14.setText("")
        self.label_13.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u043e\u0442\u0434\u0435\u043b\u043e\u0432", None))
    # retranslateUi

    def init_ui(self, MainWindow):
#        self.btn_read.clicked.connect(self.read)
#        self.btn_calculate.clicked.connect(self.calculate)
#        self.btn_request.clicked.connect(self.request_history)
#        self.btn_from_invoice.clicked.connect(self.from_invoice)
#        self.btn_save_report.clicked.connect(self.save_report)
        self.btn_save_divisions.clicked.connect(self.save_divisions)
        self.le_subscription.setText('4200')
        self.le_personal.setText('10000')
        self.le_divisions_cost.setText('900')
        self.le_minuts.setText('24000')
        self.le_cost_for_number.setText('160')
        self.tabWidget.currentChanged.connect(self.load_settings)
        self.lv_divisions.clicked.connect(self.get_info)
        self.phones = get_phones()
        self.divisions = load_divisions()
        self.set_settings(self.divisions, self.phones)
        self.btn_save_divisions.setDisabled(True)

    def set_settings(self, _divisions, _phones):
        div = _divisions['name'].tolist()
        div.sort()
        slm = QStringListModel(div)
        self.lv_divisions.setModel(slm)

    def get_info(self):
        self.btn_save_divisions.setEnabled(True)
        _id = self.divisions[self.divisions.name == self.lv_divisions.currentIndex().data()].iloc[0]['id']
        self.le_name.setText(self.lv_divisions.currentIndex().data())
        self.lineEdit_5.setText(str(_id))
        self.le_divisions.setText(str(self.divisions[self.divisions.id == _id].iloc[0]['departments']))
        self.le_personals.setText(str(self.divisions[self.divisions.id == _id].iloc[0]['employees']))

        phones_by_division = self.phones[self.phones.division_id == _id][['number', 'description']].reset_index(drop=True)
        phones_by_division.columns = ['Номер', 'Описание']
        model = PandasModel(phones_by_division)
        self.tw_phones.setModel(model)
        self.tw_phones.resizeColumnsToContents()
        # self.tw_phones.inde

    def load_settings(self):
        if self.tabWidget.currentIndex():
            pass

    def save_divisions(self):

        pass

    def from_invoice(self):
        path = QFileDialog.getOpenFileName(
            self.centralwidget,
            "Открыть файл",
            "",
            "PDF (*.pdf)"
        )
        if path[0]:
            table = parse_pdf(path[0])
            divisions_cost = 0
            personal_cost = 0
            subscription_cost = 0
            minutes_cost = 0
            for row in table:
                value = row[1].replace(',', '.').replace(' ', '')
                if 'Дополнительная группа пользователей' in row[0]:
                    divisions_cost += float(value)
                if 'Дополнительные внутренние номера' in row[0]:
                    personal_cost += float(value)
                if 'Безлимитная запись' in row[0] or \
                        'ОАТС Про' in row[0] or \
                        'Интеграция с CRM' in row[0] or \
                        'Алгоритм распред' in row[0]:
                    subscription_cost += float(value)
                if 'Минут' in row[0] or 'Соединения по сети передачи данных' in row[0]:
                    minutes_cost += float(value)
            self.le_divisions_cost.setText(str(round(divisions_cost, 2)))
            self.le_personal.setText(str(round(personal_cost, 2)))
            self.le_subscription.setText(str(round(subscription_cost, 2)))
            self.le_minuts.setText(str(round(minutes_cost, 2)))

    def save_report(self):
        s_fname = QFileDialog.getSaveFileName(
            self.centralwidget,
            "Сохранить файл",
            f'Домру_{self.end_date.date().year()}.{self.end_date.date().month()}.xlsx',
            "XLSX (*.xlsx)"
        )
        if s_fname[0]:
            self.to_model.to_excel(s_fname[0], index=False)

    def read(self):
        df = read_tel_statistic()
        start_date = str(min(df.date)).split()[0]
        end_date = str(max(df.date)).split()[0]
        y_min = int(start_date.split('-')[0])
        m_min = int(start_date.split('-')[1])
        d_min = int(start_date.split('-')[2])
        y_max = int(end_date.split('-')[0])
        m_max = int(end_date.split('-')[1])
        d_max = int(end_date.split('-')[2])
        date_min = QDate(y_min, m_min, d_min)
        date_max = QDate(y_max, m_max, d_max)
        self.start_date.setDateRange(date_min, date_max)
        self.start_date.setDate(date_min)
        self.end_date.setDateRange(date_min, date_max)
        self.end_date.setDate(date_max)
        self.start_date.setEnabled(True)
        self.end_date.setEnabled(True)
        self.btn_calculate.setEnabled(True)

    def calculate2(self, call_history):
        # Считаем затраты на подразделения (сотрудники, отделы)
        _divisions = calculate_expenses_by_divisions(
            float(self.le_personal.text()),
            float(self.le_divisions_cost.text()),
            float(self.le_subscription.text()))
        # Считаем затраты по номерам
        _phones = calculate_expenses_by_numbers2(call_history,
            float(self.le_cost_for_number.text()),
            float(self.le_minuts.text()))
        print(_phones)
        _final = _divisions.merge(_phones, on='id')
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        _final['total'] = _final['cost_for_employees'] + \
                          _final['cost_for_departments'] + \
                          _final['cost_for_subscription'] + \
                          _final['cost_for_calls'] + \
                          _final['cost_for_numbers']
        self.to_model = _final[['name', 'cost_for_employees', 'cost_for_departments', 'cost_for_subscription',
                                'cost_for_calls', 'cost_for_numbers', 'total']]
        self.to_model.columns = ['Отдел', 'Сотрудники', 'Отделы', 'Абонентка', 'Звонки', 'Номера', 'Общая сумма']
        model = PandasModel(self.to_model)
        self.tableView.setModel(model)
        # self.tableWidget.resizeRowsToContents()
        self.tableView.resizeColumnsToContents()
        self.btn_save_report.setEnabled(True)

    def request_history(self, start_date_='', end_date='', period='last_month'):
        global CALL_HISTORY
        with open(r'config/cfg.json', 'r') as f:
            text = json.load(f)
        token = text['token']
        path_to_api = text['path_to_api']
        json_history = '/crmapi/v1/history/json'
        headers = {'X-API-KEY': token}
        params = {'type': 'out'}
        # TODO
#        if start_date_ != '':
#            params['start'] = start_date_
#        if end_date != '':
#            params['end'] = end_date
        if period != '':
            params['period'] = period
        r = requests.get(path_to_api + json_history, headers=headers, params=params)
        df = pd.json_normalize(r.json())
        CALL_HISTORY = df.query('status == "success"')
        self.calculate2(df.query('status == "success"'))
#        return df.query('status == "success"')

    def calculate(self):
        _start_date = datetime.datetime(self.start_date.date().year(),
                                       self.start_date.date().month(),
                                       self.start_date.date().day())
        _end_date = datetime.datetime(self.end_date.date().year(),
                                     self.end_date.date().month(),
                                     self.end_date.date().day())
        _divisions = calculate_expenses_by_divisions(
                                                    float(self.le_personal.text()),
                                                    float(self.le_divisions_cost.text()),
                                                    float(self.le_subscription.text()))
        _phones = calculate_expenses_by_numbers(
                                                float(self.le_cost_for_number.text()),
                                                _start_date,
                                                _end_date,
                                                float(self.le_minuts.text()))
        _final = _divisions.merge(_phones, on='id')
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        _final['total'] = _final['cost_for_employees'] + \
                                _final['cost_for_departments'] + \
                                _final['cost_for_subscription'] + \
                                _final['cost_for_calls'] + \
                                _final['cost_for_numbers']
        self.to_model = _final[['name', 'cost_for_employees', 'cost_for_departments', 'cost_for_subscription',
                          'cost_for_calls', 'cost_for_numbers', 'total']]
        self.to_model.columns = ['Отдел', 'Сотрудники', 'Отделы', 'Абонентка', 'Звонки', 'Номера', 'Общая сумма']
        model = PandasModel(self.to_model)
        self.tableView.setModel(model)
        # self.tableWidget.resizeRowsToContents()
        self.tableView.resizeColumnsToContents()
        self.btn_save_report.setEnabled(True)

# from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.init_ui(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
