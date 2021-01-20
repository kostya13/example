"""
Главный модуль программы
Точка старта
"""
import loader
import click


BUBBLE = 'bubble'
INSERT = 'insert'
SELECTION = 'selection'


@click.command()
@click.option('--filename', default=None,
              help='Имя файла с несортированными данными')
@click.option('--algorithm', default=BUBBLE,
              help='Алгоритм сортировки.')
def sorter(filename, algorithm):
    """ Простая утилита для сортировки чисел
    """
    print(filename, algorithm)
    if filename is None:
        unsorted_data = loader.load_from_input()
    else:
        unsorted_data = loader.load_from_file(filename)

    allowed_algorithms = [BUBBLE, INSERT, SELECTION]
    if algorithm not in allowed_algorithms:
        print('Неправильно введено имя алгоритма')
        print('Правильные варианты:', allowed_algorithms)
        exit(1)


if __name__ == '__main__':
    sorter()