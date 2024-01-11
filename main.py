import sys

import pandas as pd
import datetime
import pdfplumber
from PySide6.QtCore import QDate, QAbstractTableModel, QModelIndex, Qt, QStringListModel

from ui_form import Ui_MainWindow
from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QFileDialog)
import requests
import json

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


class Window(QMainWindow):
    periods = {'Прошлый месяц': 'last_month',
               'Произвольный период': '',
               'Текущий месяц': 'this_month',
               'Прошлая неделя': 'last_week',
               'Текущая неделя': 'this_week',
               'Вчера': 'yesterday',
               'Сегодня': 'today'
               }
    custom_dates = False
    period = 'Прошлый месяц'
    call_history = pd.DataFrame()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.divisions = None
        self.phones = None
        self.to_model = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.add_functions()

    def add_functions(self):
        self.ui.comboBox.addItems(self.periods)
        self.ui.comboBox.currentTextChanged.connect(self.enable_dates)
        self.ui.btn_request.clicked.connect(self.request_from_api)
        self.ui.btn_from_invoice.clicked.connect(self.from_invoice)
        self.ui.btn_calculate.clicked.connect(self.calculate)
        self.ui.btn_save_report.clicked.connect(self.save_report)

        self.ui.le_subscription.setText('4500')
        self.ui.le_personal.setText('10600')
        self.ui.le_divisions_cost.setText('900')
        self.ui.le_minuts.setText('23000')
        self.ui.le_cost_for_number.setText('160')
#        self.ui.tabWidget.currentChanged.connect(self.load_settings)
        self.ui.lv_divisions.clicked.connect(self.get_info)
        self.phones = get_phones()
        self.divisions = load_divisions()
        self.set_settings(self.divisions, self.phones)
        self.ui.btn_save_divisions.setDisabled(True)

    def get_info(self):
        self.ui.btn_save_divisions.setEnabled(True)
        _id = self.divisions[self.divisions.name == self.ui.lv_divisions.currentIndex().data()].iloc[0]['id']
        self.ui.le_name.setText(self.ui.lv_divisions.currentIndex().data())
        self.ui.lineEdit_5.setText(str(_id))
        self.ui.le_divisions.setText(str(self.divisions[self.divisions.id == _id].iloc[0]['departments']))
        self.ui.le_personals.setText(str(self.divisions[self.divisions.id == _id].iloc[0]['employees']))

        phones_by_division = self.phones[self.phones.division_id == _id][['number', 'description']].reset_index(drop=True)
        phones_by_division.columns = ['Номер', 'Описание']
        model = PandasModel(phones_by_division)
        self.ui.tw_phones.setModel(model)
        self.ui.tw_phones.resizeColumnsToContents()
        # self.tw_phones.inde

    def set_settings(self, _divisions, _phones):
        div = _divisions['name'].tolist()
        div.sort()
        slm = QStringListModel(div)
        self.ui.lv_divisions.setModel(slm)

    def save_report(self):
        if self.custom_dates:
            filename = f'Домру_{self.ui.end_date.date().year()}.{self.ui.end_date.date().month()}.xlsx'
        else:
            filename = f'Домру_{datetime.datetime.today().year}.{datetime.datetime.today().month}.{datetime.datetime.today().day}.{self.period}.xlsx'
        s_fname = QFileDialog.getSaveFileName(
            self.ui.centralwidget,
            "Сохранить файл",
            filename,
            "XLSX (*.xlsx)"
        )
        if s_fname[0]:
            self.to_model.to_excel(s_fname[0], index=False)

    def calculate(self):
        # Считаем затраты на подразделения (сотрудники, отделы)
        _divisions = calculate_expenses_by_divisions(
            float(self.ui.le_personal.text()),
            float(self.ui.le_divisions_cost.text()),
            float(self.ui.le_subscription.text()))
        # Считаем затраты по номерам
        _phones = calculate_expenses_by_numbers2(self.call_history,
                                                 float(self.ui.le_cost_for_number.text()),
                                                 float(self.ui.le_minuts.text()))
#        print(_phones)
        _final = _divisions.merge(_phones, on='id')
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.setAlternatingRowColors(True)
        self.ui.tableView.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        _final['total'] = _final['cost_for_employees'] + \
                          _final['cost_for_departments'] + \
                          _final['cost_for_subscription'] + \
                          _final['cost_for_calls'] + \
                          _final['cost_for_numbers']
        self.to_model = _final[['name', 'cost_for_employees', 'cost_for_departments', 'cost_for_subscription',
                                'cost_for_calls', 'cost_for_numbers', 'total']]
        self.to_model.columns = ['Отдел', 'Сотрудники', 'Отделы', 'Абонентка', 'Звонки', 'Номера', 'Общая сумма']
        model = PandasModel(self.to_model)
        self.ui.tableView.setModel(model)
        # self.tableWidget.resizeRowsToContents()
        self.ui.tableView.resizeColumnsToContents()
        self.ui.btn_save_report.setEnabled(True)

    def from_invoice(self):
        path = QFileDialog.getOpenFileName(
            self.ui.centralwidget,
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
            self.ui.le_divisions_cost.setText(str(round(divisions_cost, 2)))
            self.ui.le_personal.setText(str(round(personal_cost, 2)))
            self.ui.le_subscription.setText(str(round(subscription_cost, 2)))
            self.ui.le_minuts.setText(str(round(minutes_cost, 2)))

    def request_from_api(self):
        try:
            if self.custom_dates:
                start_date = self.ui.start_date.date().toString('yyyyMMdd') + 'T000000Z'
                end_date = self.ui.end_date.date().toString('yyyyMMdd') + 'T235959Z'
                self.call_history = request_history(start_date_=start_date, end_date=end_date, period='')
            else:
                self.call_history = request_history(period=self.periods[self.period])
            self.ui.btn_calculate.setEnabled(True)
        except Exception:
            self.ui.btn_calculate.setEnabled(False)
            self.ui.statusbar.showMessage('Ошибка при запросе, повторите позже!', 2000)

    def enable_dates(self, text):
        self.period = text
        if text == 'Произвольный период':
            self.custom_dates = True
            self.ui.start_date.setEnabled(True)
            self.ui.start_date.setDate(QDate.currentDate().addDays(1 - QDate.currentDate().day()).addMonths(-1))
            self.ui.end_date.setEnabled(True)
            self.ui.end_date.setDate(QDate.currentDate().addDays(1 - QDate.currentDate().day()).addDays(-1))
        else:
            self.custom_dates = False
            self.ui.start_date.setEnabled(False)
            self.ui.end_date.setEnabled(False)


def request_history(start_date_='', end_date='', period='last_month'):
    with open(r'config/cfg.json', 'r') as f:
        text = json.load(f)
    token = text['token']
    path_to_api = text['path_to_api']
    json_history = '/crmapi/v1/history/json'
    headers = {'X-API-KEY': token}
    params = {'type': 'out'}
    if start_date_ != '':
        params['start'] = start_date_
    if end_date != '':
        params['end'] = end_date
    if period != '':
        params['period'] = period
    r = requests.get(path_to_api + json_history, headers=headers, params=params)
    df = pd.json_normalize(r.json())
    return df.query('status == "success"')


def calc_emp_by_divisions():
    with open(r'config/cfg.json', 'r') as f:
        text = json.load(f)
    token = text['token']
    path_to_api = text['path_to_api']
    json_users = '/crmapi/v1/users'
    headers = {'X-API-KEY': token}
    r = requests.get(path_to_api + json_users, headers=headers)
    users = json.loads(r.text)
    total_users = users['info']['limit']
    pronina = 0
    for user in users['items']:
       if (user['ext'][0] == '4'):
           pronina += 1
    return pronina, total_users


def to_seconds(val):
    val = str(val).split(':')
    return int(val[0]) * 3600 + int(val[1]) * 60 + int(val[2])


def read_tel_excel_statistic(path):
    """ Read raw data from Excel file
        :return Pandas dataset with columns:
            date: Date and time of the call
            type: type of the traffic such as:
                Входящие телефонные звонки
                Исходящие местные телефонные звонки
                Исходящие телефонные звонки
            number: telephone number
            duration: duration of the call
            caller: telephone number of another side
            region: region of another side
    """
    # Read ALL files in PATH_TO_STATISTIC folder
    df = pd.read_excel(path, skiprows=[0, 1, 2, 3, 4, 5, 6, 7, 8], dtype={'Через': 'str'})
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    df['duration'] = df['Длительность'].apply(to_seconds)

    # Make new dataset with necessary columns
    db = df[['Дата', 'Тип звонка', 'Через', 'duration',
             'Клиент']]
    # Rename columns
    db.columns = ['date', 'type', 'number', 'duration', 'caller']
    # Change type of column 'number'
    #    db['number'] = db['number'].astype('str')
    return db


def load_divisions():
    """
    Read information about divisions
    :return: dataframe with divisions
    """
    pronina, total = calc_emp_by_divisions()
    df = pd.read_csv(r'config/divisions.csv', sep=';')
    index_to_change = df[df['name'] == 'Пронина'].index[0]
    df.at[index_to_change, 'employees'] = pronina
    if df.employees.sum() != total:
        print ('somthing wrong with employees')
    return df


def filter_by_date(df, _start_date, _end_date):
    """
    :param df: dataframe to filter
    :param _start_date: first day of period
    :param _end_date: last day of period
    :return: filtered dataframe from start
    """
    delta_to_the_end_of_day = datetime.timedelta(hours=23, minutes=59, seconds=59)
    return df.loc[(df['date'] >= _start_date) & (df['date'] <= _end_date + delta_to_the_end_of_day)]


def filter_outcome_calls(df):
    """
    Returns dataframe with only outgoing calls
    :param df: dataframe to be filtered
    :return: dataframe with only outgoing calls
    """
    return df[df.type.str.contains('Исходящие')]


def calc_price_sec(df, total_cost):
    """
    Calculate cost of 1 second
    :param df: dataframe with all outgoing calls
    :param total_cost: total cost for all calls
    :return: cost of 1 second
    """
    return total_cost / df.duration.sum()


def get_phones():
    """
    Read from csv information about all telephone numbers
    :return: dataframe with phones and divisions
    """
    _phones = pd.read_csv(r'config/phones.csv', sep=';')
    _phones['number'] = _phones['number'].astype('str')
    return _phones


def calc_phones_cost_to_division(df=get_phones(), cost_per_number=160):
    """
    Calculate cost for numbers for division
    :param df: dataframe with numbers and divisions
    :param cost_per_number: cost for one number
    :return: dataframe group by division with total cost for it
    """
    temp = df.division_id.value_counts().reset_index()
    temp.columns = ['division_id', 'cost_for_number']
    temp.cost_for_number = temp.cost_for_number * cost_per_number
    return temp


def calc_employee_cost(df=load_divisions(), total_cost=10000.0):
    return round(total_cost / df.employees.sum(), 2)


def calculate_sum_for_employees(df=load_divisions(), total_cost=10000.0):
    emp = calc_employee_cost(df, total_cost)
    df['cost_for_employees'] = df['employees'] * emp


def calc_department_cost(df=load_divisions(), total_cost=900):
    return round(total_cost / df.departments.sum(), 2)


def calc_sum_for_departments(df=load_divisions(), total_cost=900):
    dep = calc_department_cost(df, total_cost)
    df['cost_for_departments'] = df['departments'] * dep


def calc_subscription_cost(df=load_divisions(), total_cost=900):
    return total_cost / df.id.count()


def calc_subscription_sum_by_departments(df=load_divisions(), total_cost=4500):
    sub = calc_subscription_cost(df, total_cost)
    df['cost_for_subscription'] = round(sub, 2)


def calculate_expenses_by_divisions(employees_cost=10160.97, departments_cost=900, subscription_fee=4500,
                                    divisions=load_divisions()):
    calculate_sum_for_employees(divisions, employees_cost)
    calc_sum_for_departments(divisions, departments_cost)
    calc_subscription_sum_by_departments(divisions, subscription_fee)
    return divisions


def calc_calls_duration():
    pass


def calculate_expenses_by_numbers2(call_history, number_cost, conversation_cost, phones=get_phones()):
    #    global CALL_HISTORY
    phones_cost = calc_phones_cost_to_division(phones, number_cost)
    #    if CALL_HISTORY.empty:
    #        return None
    # Группируем по номеру телефона
    number_seconds = call_history.groupby('diversion').duration.sum().reset_index()
    number_seconds.rename(columns={"diversion": "number"}, inplace=True)
    phone_division = phones.merge(number_seconds, on='number')
    # Группируем по подразделению и считаем общую сумму разговоров
    division_duration = phone_division.groupby('division_id').duration.sum().reset_index()
    # Считаем стоимость секунды
    sec_cost = calc_price_sec(division_duration, conversation_cost)
    # Пишем столбец со стоимостью разговоров для подразделения
    division_duration['cost_for_calls'] = round(division_duration['duration'].astype(int) * sec_cost, 2)
    # Получаем датафрейм со стоимостью звонков и номеров телефона
    merged = division_duration.merge(phones_cost, on='division_id')
    merged.columns = ['id', 'duration', 'cost_for_calls', 'cost_for_numbers']
    return merged


# def calculate_expenses_by_numbers(number_cost, start_date, end_date, conversation_cost, phones=get_phones()):
#     phones_cost = calc_phones_cost_to_division(phones, number_cost)
#     calls_statistic = read_tel_statistic()
#     filtered_by_dates_calls_statistics = \
#         filter_by_date(df=calls_statistic, _start_date=start_date, _end_date=end_date).sort_values('date')
#     # Фильтруем по направлениям звонков
#     outgoing_filtered_by_dates_calls_statistics = filter_outcome_calls(filtered_by_dates_calls_statistics)
#     # Группируем по номеру телефона
#     number_seconds = outgoing_filtered_by_dates_calls_statistics.groupby('number').duration.sum().reset_index()
#     phone_division = phones.merge(number_seconds, on='number')
#     # Группируем по подразделению и считаем общую сумму разговоров
#     division_duration = phone_division.groupby('division_id').duration.sum().reset_index()
#     # Считаем стоимость секунды
#     sec_cost = calc_price_sec(division_duration, conversation_cost)
#     # Пишем столбец со стоимостью разговоров для подразделения
#     division_duration['cost_for_calls'] = round(division_duration['duration'].astype(int) * sec_cost, 2)
#     # Получаем датафрейм со стоимостью звонков и номеров телефона
#     merged = division_duration.merge(phones_cost, on='division_id')
#     merged.columns = ['id', 'duration', 'cost_for_calls', 'cost_for_numbers']
#     return merged


def parse_pdf(path_to_pdf_file):
    with pdfplumber.open(path_to_pdf_file) as pdf:
        page = pdf.pages[0]
        table = page.extract_table()
    return table


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = Window()
    widget.show()
    sys.exit(app.exec())

    # pd.set_option('display.max_columns', None)
    # Считаем затраты на подразделения
    # divisions = calculate_expenses_by_divisions()
    # start_date = datetime.datetime(2022, 12, 1)
    # end_date = datetime.datetime(2022, 12, 31)
    # phones = calculate_expenses_by_numbers(160, start_date, end_date, 24000)
    # Получаем телефоны
    # phones = get_phones()
    # Считаем затраты на телефонные линии
    # phones_cost = calc_phones_cost_to_division(phones, 160)
    # Получаем данные по всем звонкам
    # calls_statistic = read_tel_statistic()

    # Фильтруем по датам
    # work_by_dates = filter_by_date(df=work, _start_date=start_date, _end_date=end_date).sort_values('date')
    # Фильтруем по направлениям звонков
    # work_by_dates_outcome = filter_outcome_calls(work_by_dates)
    # Группируем по номеру телефона
    # number_seconds = work_by_dates_outcome.groupby('number').duration.sum().reset_index()
    # Объединяем телефоны и продолжительность разговоров
    # phone_division = phones.merge(number_seconds, on='number')
    # Группируем по подразделению и считаем общую сумму разговоров
    # division_duration = phone_division.groupby('division_id').duration.sum().reset_index()
    # Считаем стоимость секунды
    # sec_cost = calc_price_sec(division_duration, 24000)
    # Пишем столбец со стоимостью разговоров для подразделения
    # division_duration['cost_for_calls'] = round(division_duration['duration'] * sec_cost, 2)
    # print(phones_cost)
    # print(divisions)
    # print(phones)
    # Получаем датафрейм со стоимостью звонков и номеров телефона
    # merged = division_duration.merge(phones_cost, on='division_id')
    # merged.columns = ['id', 'duration', 'cost_for_calls', 'cost_for_numbers']
    # print(merged)
    # final = divisions.merge(phones, on='id')
    # final['total'] = final['cost_for_employees'] + final['cost_for_departments'] + \
    #                  final['cost_for_subscription'] + final['cost_for_calls'] + final['cost_for_numbers']
    # final.to_csv('result.csv', encoding='UTF-8', sep=';', index=False)
    # print(final[['name', 'cost_for_employees', 'cost_for_departments', 'cost_for_subscription', 'cost_for_calls',
    #              'cost_for_numbers', 'total']])
    # print(f' Total {final.total.sum()}')
    # print(f' cost_for_numbers {final.cost_for_numbers.sum()}')
    # print(f' cost_for_calls {final.cost_for_calls.sum()}')
    # print(f' cost_for_subscription {final.cost_for_subscription.sum()}')
    # print(f' cost_for_employees {final.cost_for_employees.sum()}')
    # print(f' cost_for_departments {final.cost_for_departments.sum()}')
