print('*' * 8 + ' ' + 'Игра Крестики-нолики!!!' + ' ' + '*' * 8)
print()
print('Первые ходят крестики!')
print()

def players():
    player_1 = input('Первый игрок, введите Ваше имя: ')
    player_2 = input('Второй игрок, введите Ваше имя: ')
    print('-' * 25, '\n Первый игрок - ', player_1)
    print('-' * 25, '\n Второй игрок - ', player_2)
    print('-' * 25)
    print('* ' * 18)


field = list(range(1, 10))


def playing_field(field):
    print('-' * 13)
    for i in range(3):
        print('|', field[0 + i * 3], '|', field[1 + i * 3], '|', field[2 + i * 3], '|')
        print('-' * 13)



def take_val(player_token):
    valid = False
    while not valid:
        try:
            answer = int(input(' Выбирайте клеточку от 1 до 9! \n'))
        except ValueError:
            print(' Введите верные данные!/n')
            continue
        if 1 <= answer <= 9:
            if str(field[answer - 1]) not in 'XO':
                field[answer - 1] = player_token
                print(' Вы выбрали - ' + str(answer))
                valid = True
            else:
                print(' Клетка уже занята!\n')  
        else:
            print(' Укажите число в указанном диапазоне!\n')     
        
            

def counter_win(field):
    win_tuple = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_tuple:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False



def main(field):
    counter = 0
    win = False
    while not win:
        playing_field(field)
        if counter % 2 == 0:
            take_val("X")
        else:
            take_val("O")
        counter += 1

        tmp = counter_win(field)
        if tmp:
            print(tmp, "Выиграл!")
            win = True
            break
        if counter == 9:
            print("Ничья!")
            break
    playing_field(field)


main(field)

input("Нажмите Enter для выхода!")

