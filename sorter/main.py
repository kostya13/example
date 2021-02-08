"""
Главный модуль программы
Точка старта
"""
from sorter import loader, sorting
import click


BUBBLE = 'b'
INSERT = 'i'
SELECTION = 's'


@click.command()
@click.option('--filename', default=None,
              help='Имя файла с несортированными данными')
@click.option('--algorithm', default=BUBBLE,
              help='Алгоритм сортировки.')
def sorter(filename, algorithm):
    """ Простая утилита для сортировки чисел
    """
    allowed_algorithms = [BUBBLE, INSERT, SELECTION]
    if algorithm not in allowed_algorithms:
        print('Неправильно введено имя алгоритма')
        print('Правильные варианты:', allowed_algorithms)
        exit(1)

    if filename is None:
        unsorted_data = loader.load_from_input()
    else:
        unsorted_data = loader.load_from_file(filename)

    if algorithm == BUBBLE:
        sorted_data = sorting.bubble_sort(unsorted_data)
    elif algorithm == INSERT:
        sorted_data = sorting.insert_sort(unsorted_data)
    elif algorithm == SELECTION:
        sorted_data = sorting.selection_sort(unsorted_data)

    print('Несортированный массив:', *unsorted_data)
    print('Сортированный массив:  ', *sorted_data)


if __name__ == '__main__':
    sorter()