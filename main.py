import pandas as pd
from pathlib import Path
import datetime

PATH_TO_STATISTIC = Path(r"tel_data/")


def read_tel_statistic():
    """ Read raw data from csv files
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
    df = (pd.concat(
        [pd.read_csv(f, sep=';', parse_dates=['Дата и время'], dayfirst=True)
         for f in PATH_TO_STATISTIC.glob("*.csv")], ignore_index=True))
    # Drop duplicates
    df.drop_duplicates(inplace=True)
    # Make new dataset with necessary columns
    db = df[['Дата и время', 'Тип трафика', 'Источник трафика', 'Продолжительность сек/байт',
             'Вызываемый/вызывающий номер', 'Регион']]
    # Rename columns
    db.columns = ['date', 'type', 'number', 'duration', 'caller', 'region']
    # Change type of column 'number'
    db['number'] = db['number'].astype('str')
    return db


def load_divisions():
    """
    Read information about divisions
    :return: dataframe with divisions
    """
    df = pd.read_csv(r'config/divisions.csv', sep=';')
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
    return total_cost / df.employees.sum()


def calculate_sum_for_employees(df=load_divisions(), total_cost=10000.0):
    emp = calc_employee_cost(df, total_cost)
    df['cost_for_employees'] = round(df['employees'] * emp, 2)


def calc_department_cost(df=load_divisions(), total_cost=900):
    return total_cost / df.departments.sum()


def calc_sum_for_departments(df=load_divisions(), total_cost=900):
    dep = calc_department_cost(df, total_cost)
    df['cost_for_departments'] = round(df['departments'] * dep, 2)


def calc_subscription_cost(df=load_divisions(), total_cost=900):
    return total_cost / df.id.count()


def calc_subscription_sum_by_departments(df=load_divisions(), total_cost=4200):
    sub = calc_subscription_cost(df, total_cost)
    df['cost_for_subscription'] = round(sub, 2)


def calculate_expenses_by_divisions(employees_cost=10160.97, departments_cost=900, subscription_fee=4200,
                                    divisions=load_divisions()):
    calculate_sum_for_employees(divisions, employees_cost)
    calc_sum_for_departments(divisions, departments_cost)
    calc_subscription_sum_by_departments(divisions, subscription_fee)
    return divisions


def calc_calls_duration():
    pass


def calculate_expenses_by_numbers(number_cost, start_date, end_date, conversation_cost, phones=get_phones()):
    phones_cost = calc_phones_cost_to_division(phones, number_cost)
    calls_statistic = read_tel_statistic()
    filtered_by_dates_calls_statistics = \
        filter_by_date(df=calls_statistic, _start_date=start_date, _end_date=end_date).sort_values('date')
    # Фильтруем по направлениям звонков
    outgoing_filtered_by_dates_calls_statistics = filter_outcome_calls(filtered_by_dates_calls_statistics)
    # Группируем по номеру телефона
    number_seconds = outgoing_filtered_by_dates_calls_statistics.groupby('number').duration.sum().reset_index()
    phone_division = phones.merge(number_seconds, on='number')
    # Группируем по подразделению и считаем общую сумму разговоров
    division_duration = phone_division.groupby('division_id').duration.sum().reset_index()
    # Считаем стоимость секунды
    sec_cost = calc_price_sec(division_duration, conversation_cost)
    # Пишем столбец со стоимостью разговоров для подразделения
    division_duration['cost_for_calls'] = round(division_duration['duration'] * sec_cost, 2)
    # Получаем датафрейм со стоимостью звонков и номеров телефона
    merged = division_duration.merge(phones_cost, on='division_id')
    merged.columns = ['id', 'duration', 'cost_for_calls', 'cost_for_numbers']
    return merged


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    # Считаем затраты на подразделения
    divisions = calculate_expenses_by_divisions()
    start_date = datetime.datetime(2022, 12, 1)
    end_date = datetime.datetime(2022, 12, 31)
    phones = calculate_expenses_by_numbers(160, start_date, end_date, 24000)
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
    print(divisions)
    print(phones)
    # Получаем датафрейм со стоимостью звонков и номеров телефона
    # merged = division_duration.merge(phones_cost, on='division_id')
    # merged.columns = ['id', 'duration', 'cost_for_calls', 'cost_for_numbers']
    # print(merged)
    final = divisions.merge(phones, on='id')
    final['total'] = final['cost_for_employees'] + final['cost_for_departments'] +\
                     final['cost_for_subscription'] + final['cost_for_calls'] + final['cost_for_numbers']
    final.to_csv('result.csv', encoding='UTF-8', sep=';', index=False)
    print(final[['name', 'cost_for_employees', 'cost_for_departments', 'cost_for_subscription', 'cost_for_calls', 'cost_for_numbers', 'total']])
    print(f' Total {final.total.sum()}')
    print(f' cost_for_numbers {final.cost_for_numbers.sum()}')
    print(f' cost_for_calls {final.cost_for_calls.sum()}')
    print(f' cost_for_subscription {final.cost_for_subscription.sum()}')
    print(f' cost_for_employees {final.cost_for_employees.sum()}')
    print(f' cost_for_departments {final.cost_for_departments.sum()}')