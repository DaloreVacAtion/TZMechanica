from file_creator import file_creator

str_bool = True
col_bool = True


def columns_input(user_input: str):
    if user_input.lower() == 'стоп' or user_input.lower() == 'stop':
        raise SystemExit('Производим выход из программы...')

    try:
        user_input = int(user_input)
    except ValueError as e:
        e.args += ('Формат введенных данных может принимать только числовые значения',)
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
        e.args += ('Формат введенных данных может принимать только числовые значения',)
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


if __name__ == '__main__':
    start()
