from rich import print
from rich.panel import Panel

print(Panel.fit('Крестики и нолики', title='Добро пожаловать'))

cell = list(range(1, 10))  # Создаем список от 0 до 9


# Рисуем поле
def draw_cell():
    print('-------------')
    for i in range(3):
        print('|', cell[0 + i * 3], '|', cell[1 + i * 3], '|', cell[2 + i * 3], '|')
    print('-------------')


# Создаем функцию по информации, введенной от пользователя, в которой проверяется, что ввел и свободна личейка...
def take_input(players):
    while True:
        value = input('Укажите номер ячейки:' + players)
        if not (value in '123456789'):
            print('Ввели неверно. Повторите.')
            continue
        value = int(value)
        if str(cell[value - 1]) in 'X0':
            print('Ячейка уже заполнена')
            continue
        cell[value - 1] = players
        break


wins = [(1, 2, 3), (4, 5, 6), (9, 8, 7), (1, 4, 7), (8, 5, 2), (6, 9, 3), (1, 5, 9), (7, 5, 3)]  # Выигрышные комбинации


# Создаем функцию по проверке выигрышных комбинаций
def check_win():
    for a in wins:
        if (cell[a[0] - 1]) == (cell[a[1] - 1]) == (cell[a[2] - 1]):
            return cell[a[1] - 1]
    else:
        return False


# Описываем ход игры
def main():
    counter = 0
    while True:
        draw_cell()
        if counter % 2 == 0:  # Если число четное, то ставим х
            take_input('X')
        else:
            take_input('O')  # Иначе о
        if counter > 3:
            winner = check_win()
            if winner:
                draw_cell()
                print(winner, 'Выиграл!')
                break
        counter += 1
        if counter > 8:
            draw_cell()
            print('Ничья')
            break


main()
