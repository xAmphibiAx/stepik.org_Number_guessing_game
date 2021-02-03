from random import randint


def is_valid(num, li):
    return num.isdigit() and int(num) in range(1, 101) and li.isdigit()


def answer():
    while True:
        answer = input('Сыграем еще? Да или Нет?: ')
        if answer.lower().strip() == 'да':
            game()
        if answer.lower().strip() == 'нет':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break


def game():
    print('Добро пожаловать в числовую угадайку')
    limit = input('До какого предела загадывать число?: ')
    x = randint(1, int(limit))
    count = 0
    while True:
        n = input(f'Введите число от 1 до {limit}: ')

        if not is_valid(n, limit):
            print(f'А может быть все-таки введем целое число от 1 до {limit}?')

        n = int(n)
        if n < x:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            count += 1
            continue
        if n > x:
            print('Ваше число больше загаданного, попробуйте еще разок')
            count += 1
            continue
        if n == x:
            print('Вы угадали, поздравляем!')
            count += 1
            print(f'Число попыток {count}')
            print("Хотите сыграть еще разок?) Да/Нет")
            break


game()
answer()
