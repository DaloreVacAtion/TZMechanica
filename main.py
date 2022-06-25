from file_creator import file_creator
from data_processing import (
    csv_reader,
    euclidean_distance,
    histogram
)

str_bool = True
col_bool = True


def columns_input(user_input: str):
    if user_input.lower() == 'стоп' or user_input.lower() == 'stop':
        raise SystemExit('Производим выход из программы...')

    try:
        user_input = int(user_input)
    except ValueError as e:
        e.args += ('Формат введенных данных может принимать только целочисленные значения',)
        raise

    if not 10 < user_input <= 50:
        print('К сожалению, количество столбцов может принимать значение только от 11 до 50. Пожалуйста, введите '
              'корректные данные, либо слово СТОП(STOP) для остановки программы')
    else:
        global col_bool
        col_bool = False
        return user_input


def strings_input(user_input: str):
    if user_input.lower() == 'стоп' or user_input.lower() == 'stop':
        raise SystemExit('Производим выход из программы...')

    try:
        user_input = int(user_input)
    except ValueError as e:
        e.args += ('Формат введенных данных может принимать только целочисленные значения',)
        raise

    if not 500 < user_input <= 1000:
        print('К сожалению, количество строк может принимать значение только от 501 до 1000. Пожалуйста, введите '
              'корректные данные, либо слово СТОП(STOP) для остановки программы')
    else:
        global str_bool
        str_bool = False
        return user_input


def start():
    while str_bool:
        str_input = input('Введите количество строк от 501 до 1000, либо слово СТОП(STOP) для остановки программы...\n')
        strings = strings_input(str_input)

    while col_bool:
        col_input = input('Введите количество столбцов от 11 до 50, либо слово СТОП(STOP) для остановки программы...\n')
        columns = columns_input(col_input)

    file_creator(strings, columns)
    vectors = csv_reader()
    max_dist, couple_max, min_dist, couple_min, graph = euclidean_distance(vectors)
    print(f'Максимальное расстояние: {max_dist}. Пары векторов {couple_max[0]}-{couple_max[1]}\n'
          f'Минимальное расстояние: {min_dist}. Пары векторов {couple_min[0]}-{couple_min[1]}')
    histogram(graph, max_dist)


if __name__ == '__main__':
    start()
